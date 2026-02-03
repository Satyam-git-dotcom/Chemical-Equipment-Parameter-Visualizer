import pandas as pd

def analyze_csv(file):
    df = pd.read_csv(file)

    summary = {
        "total_equipment": len(df),
        "avg_flowrate": round(df["Flowrate"].mean(), 2),
        "avg_pressure": round(df["Pressure"].mean(), 2),
        "avg_temperature": round(df["Temperature"].mean(), 2),
        "equipment_distribution": df["Type"].value_counts().to_dict()
    }

    return summary