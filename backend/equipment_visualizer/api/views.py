import os
import tempfile
import matplotlib.pyplot as plt

from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Dataset
from .utils import analyze_csv

class UploadCSVView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        try:
            summary = analyze_csv(file)

            Dataset.objects.create(
                name=file.name,
                summary=summary
            )

            return Response(summary)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=400
            )
    
class HistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        datasets = Dataset.objects.order_by('-uploaded_at')[:5]

        data = [
            {
                "name": d.name,
                "uploaded_at": d.uploaded_at,
                "summary": d.summary
            }
            for d in datasets
        ]

        return Response(data)
    
def generate_charts(dataset):
    temp_dir = tempfile.mkdtemp()

    distribution = dataset.equipment_distribution

    labels = list(distribution.keys())
    values = list(distribution.values())

    # --- BAR CHART ---
    bar_path = os.path.join(temp_dir, "bar.png")
    plt.figure()
    plt.bar(labels, values)
    plt.title("Equipment Distribution")
    plt.tight_layout()
    plt.savefig(bar_path)
    plt.close()

    # --- PIE CHART ---
    pie_path = os.path.join(temp_dir, "pie.png")
    plt.figure()
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Equipment Share")
    plt.tight_layout()
    plt.savefig(pie_path)
    plt.close()

    # --- LINE CHART ---
    line_path = os.path.join(temp_dir, "line.png")
    plt.figure()
    plt.plot(
        ["Flowrate", "Pressure", "Temperature"],
        [
            dataset.avg_flowrate,
            dataset.avg_pressure,
            dataset.avg_temperature
        ],
        marker="o"
    )
    plt.title("Average Parameters")
    plt.tight_layout()
    plt.savefig(line_path)
    plt.close()

    return bar_path, pie_path, line_path
    
from django.http import FileResponse
from .pdf_utils import generate_pdf

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class PDFReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, dataset_id):
        dataset = Dataset.objects.get(id=dataset_id)

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = "attachment; filename=equipment_report.pdf"

        doc = SimpleDocTemplate(response, pagesize=A4)
        styles = getSampleStyleSheet()
        elements = []

        elements.append(Paragraph("<b>Chemical Equipment Report</b>", styles["Title"]))
        elements.append(Paragraph(f"Total Equipment: {dataset.total_equipment}", styles["Normal"]))
        elements.append(Paragraph(f"Average Flowrate: {dataset.avg_flowrate}", styles["Normal"]))
        elements.append(Paragraph(f"Average Pressure: {dataset.avg_pressure}", styles["Normal"]))
        elements.append(Paragraph(f"Average Temperature: {dataset.avg_temperature}", styles["Normal"]))

        # --- GENERATE CHARTS ---
        bar, pie, line = generate_charts(dataset)

        elements.append(Paragraph("<b>Equipment Distribution</b>", styles["Heading2"]))
        elements.append(Image(bar, width=400, height=300))

        elements.append(Paragraph("<b>Equipment Share</b>", styles["Heading2"]))
        elements.append(Image(pie, width=400, height=300))

        elements.append(Paragraph("<b>Average Parameters Trend</b>", styles["Heading2"]))
        elements.append(Image(line, width=400, height=300))

        doc.build(elements)
        return response
    
class HistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        datasets = Dataset.objects.order_by("-uploaded_at")[:5]

        data = [
            {
                "id": d.id,
                "name": d.name,
                "uploaded_at": d.uploaded_at.strftime("%Y-%m-%d %H:%M:%S"),
                "summary": d.summary
            }
            for d in datasets
        ]

        return Response(data)