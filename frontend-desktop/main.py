import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QFileDialog
)
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000/api/upload/"
USERNAME = "satyamDjango"
PASSWORD = "Django@123"


class EquipmentVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Parameter Visualizer")
        self.setGeometry(200, 200, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel("Upload CSV file to analyze equipment data")
        self.layout.addWidget(self.label)

        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.clicked.connect(self.upload_csv)
        self.layout.addWidget(self.upload_btn)

        self.setLayout(self.layout)

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        with open(file_path, "rb") as f:
            response = requests.post(
                API_URL,
                files={"file": f},
                auth=(USERNAME, PASSWORD)
            )

        if response.status_code == 200:
            data = response.json()
            self.show_summary(data)
            self.show_chart(data["equipment_distribution"])
        else:
            self.label.setText("Upload failed")

    def show_summary(self, data):
        summary_text = (
            f"Total Equipment: {data['total_equipment']}\n"
            f"Avg Flowrate: {data['avg_flowrate']}\n"
            f"Avg Pressure: {data['avg_pressure']}\n"
            f"Avg Temperature: {data['avg_temperature']}"
        )
        self.label.setText(summary_text)

    def show_chart(self, distribution):
        types = list(distribution.keys())
        counts = list(distribution.values())

        plt.figure(figsize=(6, 4))
        plt.bar(types, counts)
        plt.title("Equipment Type Distribution")
        plt.xlabel("Equipment Type")
        plt.ylabel("Count")
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentVisualizer()
    window.show()
    sys.exit(app.exec_())