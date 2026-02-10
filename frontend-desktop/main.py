import sys
import requests

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QTabWidget,
    QSizePolicy, QFrame, QMessageBox, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

API_UPLOAD_URL = "http://127.0.0.1:8000/api/upload/"
API_HISTORY_URL = "http://127.0.0.1:8000/api/history/"
API_PDF_URL = "http://127.0.0.1:8000/api/report/"

class ChartWidget(FigureCanvas):
    def __init__(self, title):
        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        super().__init__(self.figure)
        self.ax.set_title(title)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def clear(self):
        self.ax.clear()

    def draw_bar(self, labels, values):
        self.clear()
        self.ax.bar(labels, values)
        self.figure.tight_layout()
        self.draw()

    def draw_pie(self, labels, values):
        self.clear()
        self.ax.pie(values, labels=labels, autopct="%1.1f%%")
        self.figure.tight_layout()
        self.draw()

    def draw_line(self, labels, values):
        self.clear()
        self.ax.plot(labels, values, marker="o")
        self.figure.tight_layout()
        self.draw()


class EquipmentVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Parameter Visualizer")
        self.setMinimumSize(900, 600)

        self.dataset_id = None

        self.tabs = QTabWidget()
        self.analytics_tab = QWidget()
        self.history_tab = QWidget()

        self.tabs.addTab(self.analytics_tab, "Analytics")
        self.tabs.addTab(self.history_tab, "History")

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

        self.setup_analytics_ui()
        self.setup_history_ui()
        self.load_history()

    # ---------- ANALYTICS TAB ----------
    def setup_analytics_ui(self):
        layout = QVBoxLayout()

        top = QHBoxLayout()
        upload_btn = QPushButton("Upload CSV")
        upload_btn.clicked.connect(self.upload_csv)

        self.pdf_btn = QPushButton("Download PDF")
        self.pdf_btn.setEnabled(False)
        self.pdf_btn.clicked.connect(self.download_pdf)

        top.addWidget(upload_btn)
        top.addWidget(self.pdf_btn)
        top.addStretch()
        layout.addLayout(top)

        self.summary = QLabel("Upload a CSV to view analytics")
        self.summary.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.summary.setWordWrap(True)
        layout.addWidget(self.summary)

        charts_row = QHBoxLayout()
        self.bar = ChartWidget("Equipment Distribution")
        self.pie = ChartWidget("Equipment Share")
        charts_row.addWidget(self.bar)
        charts_row.addWidget(self.pie)

        self.line = ChartWidget("Average Parameters")

        layout.addLayout(charts_row)
        layout.addWidget(self.line)

        self.analytics_tab.setLayout(layout)

    # ---------- HISTORY TAB ----------
    def setup_history_ui(self):
        layout = QVBoxLayout()
        self.history_list = QListWidget()
        self.history_list.itemClicked.connect(self.load_from_history)
        layout.addWidget(QLabel("Last 5 Uploaded Datasets"))
        layout.addWidget(self.history_list)
        self.history_tab.setLayout(layout)

    def load_history(self):
        try:
            r = requests.get(API_HISTORY_URL, timeout=10)
            if r.status_code == 200:
                self.history_list.clear()
                history_data = r.json()

                if not history_data:
                    self.history_list.addItem("No history available")
                    return

                for d in history_data:
                    item = QListWidgetItem(
                        f"{d.get('uploaded_at', 'N/A')} | {d.get('name', 'dataset')} (ID: {d.get('id')})"
                    )
                    item.setData(Qt.UserRole, d)
                    self.history_list.addItem(item)
            else:
                QMessageBox.warning(
                    self, "History Error", f"Failed to load history ({r.status_code})"
                )
        except Exception as e:
            QMessageBox.critical(self, "History Error", str(e))

    def load_from_history(self, item):
        history_data = item.data(Qt.UserRole)
        self.dataset_id = history_data.get("id")

        if not self.dataset_id:
            QMessageBox.warning(self, "Error", "Invalid dataset selected")
            return

        self.pdf_btn.setEnabled(True)

        summary = history_data.get("summary")
        if summary:
            self.update_dashboard(summary)

    # ---------- API ACTIONS ----------
    def upload_csv(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Upload CSV", "", "CSV Files (*.csv)"
        )
        if not path:
            return

        try:
            with open(path, "rb") as f:
                r = requests.post(
                    API_UPLOAD_URL,
                    files={"file": f},
                    timeout=10
                )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        if r.status_code == 200:
            data = r.json()

            self.update_dashboard(data)
            self.dataset_id = data.get("dataset_id")
            self.pdf_btn.setEnabled(self.dataset_id is not None)
            self.load_history()

            QMessageBox.information(
                self,
                "Upload Successful",
                "CSV uploaded successfully. Analytics loaded."
            )
        else:
            QMessageBox.warning(self, "Error", "Upload failed")

    def download_pdf(self):
        if not self.dataset_id:
            QMessageBox.warning(
                self,
                "No Dataset Selected",
                "Please select a dataset from the History tab before downloading the PDF."
            )
            return

        save, _ = QFileDialog.getSaveFileName(
            self, "Save PDF", "equipment_report.pdf", "PDF Files (*.pdf)"
        )
        if not save:
            return

        try:
            r = requests.get(
                f"{API_PDF_URL}{self.dataset_id}/",
                timeout=10
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        if r.status_code == 200:
            with open(save, "wb") as f:
                f.write(r.content)
            QMessageBox.information(self, "Success", "PDF downloaded successfully")
        else:
            QMessageBox.warning(
                self,
                "Download Failed",
                f"Server returned status {r.status_code}"
            )

    # ---------- UPDATE DASHBOARD ----------
    def update_dashboard(self, data):
        if not data:
            return

        dist = data.get("equipment_distribution", {})
        self.bar.draw_bar(dist.keys(), dist.values())
        self.pie.draw_pie(dist.keys(), dist.values())
        self.line.draw_line(
            ["Flowrate", "Pressure", "Temperature"],
            [
                data.get("avg_flowrate", 0),
                data.get("avg_pressure", 0),
                data.get("avg_temperature", 0)
            ]
        )

        self.summary.setText(
            f"Total Equipment: {data.get('total_equipment', 0)}\n"
            f"Avg Flowrate: {data.get('avg_flowrate', 0)}\n"
            f"Avg Pressure: {data.get('avg_pressure', 0)}\n"
            f"Avg Temperature: {data.get('avg_temperature', 0)}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentVisualizer()
    window.show()
    sys.exit(app.exec_())