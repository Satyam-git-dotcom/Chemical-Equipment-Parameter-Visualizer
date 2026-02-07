import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend
);

function AverageChart({ summary }) {
  if (!summary) return null;

  const data = {
    labels: ["Flowrate", "Pressure", "Temperature"],
    datasets: [
      {
        label: "Average Values",
        data: [
          summary.avg_flowrate,
          summary.avg_pressure,
          summary.avg_temperature,
        ],
        backgroundColor: ["#1cc88a", "#36b9cc", "#f6c23e"],
      },
    ],
  };

  return (
    <div style={{ marginTop: "30px" }}>
      <h3>Average Parameter Values</h3>
      <Bar data={data} />
    </div>
  );
}

export default AverageChart;