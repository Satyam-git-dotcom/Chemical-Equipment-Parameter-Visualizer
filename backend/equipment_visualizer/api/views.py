from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Dataset
from .utils import analyze_csv

class UploadCSVView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        summary = analyze_csv(file)

        Dataset.objects.create(
            name=file.name,
            summary=summary
        )

        return Response(summary)
    
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