from django.urls import path
from .views import UploadCSVView, HistoryView

urlpatterns = [
    path("upload/", UploadCSVView.as_view(), name="upload-csv"),
    path("history/", HistoryView.as_view(), name="upload-history"),
]