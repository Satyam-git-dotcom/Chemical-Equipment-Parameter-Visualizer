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
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        try:
            summary = analyze_csv(file)

            dataset = Dataset.objects.create(
                name=file.name,
                summary=summary
            )

            return Response({
                "dataset_id": dataset.id,
                **summary
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=400
            )
    
    
def generate_charts(dataset):
    temp_dir = tempfile.mkdtemp()

    summary = dataset.summary or {}
    if isinstance(summary, str):
        import json
        summary = json.loads(summary)

    distribution = summary.get("equipment_distribution", {})

    labels = list(distribution.keys())
    values = list(distribution.values())

    # --- BAR CHART ---
    bar_path = os.path.join(temp_dir, "bar.png")
    plt.figure()
    if labels and values:
        plt.bar(labels, values)
    plt.title("Equipment Distribution")
    plt.tight_layout()
    plt.savefig(bar_path)
    plt.close()

    # --- PIE CHART ---
    pie_path = os.path.join(temp_dir, "pie.png")
    plt.figure()
    if values:
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
            summary.get("avg_flowrate", 0),
            summary.get("avg_pressure", 0),
            summary.get("avg_temperature", 0),
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
    permission_classes = []

    def get(self, request, dataset_id):
        try:
            dataset = Dataset.objects.get(id=dataset_id)
        except Dataset.DoesNotExist:
            return Response({"error": "Dataset not found"}, status=404)

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="equipment_report_{dataset_id}.pdf"'

        doc = SimpleDocTemplate(response, pagesize=A4)
        styles = getSampleStyleSheet()
        elements = []

        elements.append(Paragraph("<b>Chemical Equipment Report</b>", styles["Title"]))
        elements.append(Paragraph(f"Dataset ID: {dataset.id}", styles["Normal"]))

        summary = dataset.summary
        if isinstance(summary, str):
            import json
            summary = json.loads(summary)

        elements.append(Paragraph(f"Total Equipment: {summary.get('total_equipment')}", styles["Normal"]))
        elements.append(Paragraph(f"Average Flowrate: {summary.get('avg_flowrate')}", styles["Normal"]))
        elements.append(Paragraph(f"Average Pressure: {summary.get('avg_pressure')}", styles["Normal"]))
        elements.append(Paragraph(f"Average Temperature: {summary.get('avg_temperature')}", styles["Normal"]))

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
    permission_classes = []

    def get(self, request):
        datasets = Dataset.objects.order_by("-uploaded_at")[:5]
        data = [
            {
                "id": d.id,
                "name": d.name,
                "uploaded_at": d.uploaded_at.strftime("%Y-%m-%d %H:%M:%S"),
                "summary": d.summary,
            }
            for d in datasets
        ]
        return Response(data)