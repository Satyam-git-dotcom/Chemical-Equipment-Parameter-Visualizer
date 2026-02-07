
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
    
from django.http import FileResponse
from .pdf_utils import generate_pdf

class PDFReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, dataset_id=None):
        if dataset_id:
            dataset = Dataset.objects.get(id=dataset_id)
        else:
            dataset = Dataset.objects.order_by("-uploaded_at").first()

        pdf = generate_pdf(dataset)
        return FileResponse(pdf, as_attachment=True, filename="equipment_report.pdf")
    
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