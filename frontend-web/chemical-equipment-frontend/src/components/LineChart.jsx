import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip,
  Legend
);

function LineChart({ summary, dark }) {
  if (!summary) return null;

  const data = {
    labels: ["Flowrate", "Pressure", "Temperature"],
    datasets: [
      {
        label: "Average Trend",
        data: [
          summary.avg_flowrate,
          summary.avg_pressure,
          summary.avg_temperature,
        ],
        borderColor: dark ? "#36b9cc" : "#4e73df",
        backgroundColor: "transparent",
      },
    ],
  };

  return (
  <div
    style={{
      marginTop: "30px",
      background: dark ? "#1f1f1f" : "#fafafa",
      padding: "20px",
      borderRadius: "8px",
    }}
  >
    <h3 style={{ textAlign: "center" }}>
      Average Parameters Trend
    </h3>
    <Line data={data} />
  </div>
)
};

export default LineChart;