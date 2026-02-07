from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime


def generate_pdf(dataset):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    y = height - 50

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Chemical Equipment Parameter Report")

    y -= 30
    p.setFont("Helvetica", 11)
    p.drawString(50, y, f"Dataset Name: {dataset.name}")
    y -= 20
    p.drawString(50, y, f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y -= 30
    summary = dataset.summary

    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Summary Statistics")
    y -= 20

    p.setFont("Helvetica", 11)
    p.drawString(50, y, f"Total Equipment: {summary['total_equipment']}")
    y -= 15
    p.drawString(50, y, f"Average Flowrate: {summary['avg_flowrate']}")
    y -= 15
    p.drawString(50, y, f"Average Pressure: {summary['avg_pressure']}")
    y -= 15
    p.drawString(50, y, f"Average Temperature: {summary['avg_temperature']}")

    y -= 30
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Equipment Type Distribution")
    y -= 20

    p.setFont("Helvetica", 11)
    for eq_type, count in summary["equipment_distribution"].items():
        p.drawString(50, y, f"{eq_type}: {count}")
        y -= 15

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer