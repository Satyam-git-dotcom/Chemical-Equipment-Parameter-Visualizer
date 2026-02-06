import pandas as pd

def analyze_csv(file):
    try:
        file.seek(0)
        df = pd.read_csv(file)

        required_columns = ["Equipment Name", "Type", "Flowrate", "Pressure", "Temperature"]

        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        summary = {
            "total_equipment": int(len(df)),
            "avg_flowrate": float(round(df["Flowrate"].mean(), 2)),
            "avg_pressure": float(round(df["Pressure"].mean(), 2)),
            "avg_temperature": float(round(df["Temperature"].mean(), 2)),
            "equipment_distribution": df["Type"].value_counts().to_dict()
        }

        return summary

    except Exception as e:
        # This makes the error visible instead of 500 crash
        raise RuntimeError(f"CSV processing error: {str(e)}")