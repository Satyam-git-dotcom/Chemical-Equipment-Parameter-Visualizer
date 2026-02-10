from django.urls import path
from .views import UploadCSVView, HistoryView, PDFReportView

urlpatterns = [
    path("upload/", UploadCSVView.as_view(), name="upload"),
    path("history/", HistoryView.as_view(), name="history"),
    path("report/", PDFReportView.as_view()),
    path("report/<int:dataset_id>/", PDFReportView.as_view(), name="report"),
]