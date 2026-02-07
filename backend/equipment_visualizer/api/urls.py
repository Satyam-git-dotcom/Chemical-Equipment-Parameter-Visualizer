from django.urls import path
from .views import UploadCSVView, HistoryView, PDFReportView

urlpatterns = [
    path("upload/", UploadCSVView.as_view()),
    path("history/", HistoryView.as_view()),
    path("report/", PDFReportView.as_view()),
    path("report/<int:dataset_id>/", PDFReportView.as_view()),
]