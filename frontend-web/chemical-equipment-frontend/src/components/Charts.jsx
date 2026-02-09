import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar, Pie } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend
);

function Charts({ distribution, dark }) {
  if (!distribution) return null;

  const labels = Object.keys(distribution);
  const values = Object.values(distribution);

  const colors = dark
    ? ["#22d3ee", "#34d399", "#fbbf24", "#f87171", "#a78bfa"]
    : ["#2563eb", "#059669", "#0ea5e9", "#f59e0b", "#dc2626"];

  const chartData = {
    labels,
    datasets: [
      {
        label: "Equipment Count",
        data: values,
        backgroundColor: colors,
        borderRadius: 6,
      },
    ],
  };

  const exportChart = () => {
    const canvas = document.querySelector("canvas");
    if (!canvas) return;
    const link = document.createElement("a");
    link.download = "equipment_distribution.png";
    link.href = canvas.toDataURL("image/png");
    link.click();
  };

  return (
    <div style={{ marginTop: "32px" }}>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: "16px",
          flexWrap: "wrap",
          gap: "12px",
        }}
      >
        <h3 style={{ margin: 0 }}>Equipment Distribution</h3>

        <button
          onClick={exportChart}
          style={{
            padding: "8px 14px",
            borderRadius: "8px",
            border: "none",
            cursor: "pointer",
            background: dark ? "#374151" : "#eef2ff",
            color: dark ? "#e5e7eb" : "#1e3a8a",
            fontWeight: 600,
          }}
        >
          📊 Export Chart
        </button>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
          gap: "24px",
        }}
      >
        <div
          style={{
            background: dark ? "#111827" : "#f9fafb",
            padding: "20px",
            borderRadius: "14px",
          }}
        >
          <h4 style={{ textAlign: "center", marginBottom: "10px" }}>
            Bar Chart
          </h4>
          <Bar data={chartData} />
        </div>

        <div
          style={{
            background: dark ? "#111827" : "#f9fafb",
            padding: "20px",
            borderRadius: "14px",
          }}
        >
          <h4 style={{ textAlign: "center", marginBottom: "10px" }}>
            Pie Chart
          </h4>
          <Pie data={chartData} />
        </div>
      </div>
    </div>
  );
}

export default Charts;