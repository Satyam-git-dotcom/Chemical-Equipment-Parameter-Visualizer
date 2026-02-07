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
    ? ["#36b9cc", "#1cc88a", "#f6c23e", "#e74a3b"]
    : ["#4e73df", "#1cc88a", "#36b9cc", "#f6c23e"];

  const data = {
    labels,
    datasets: [
      {
        label: "Equipment Count",
        data: values,
        backgroundColor: colors,
      },
    ],
  };

  const exportChart = () => {
    const canvas = document.querySelector("canvas");
    const link = document.createElement("a");
    link.download = "equipment_chart.png";
    link.href = canvas.toDataURL();
    link.click();
  };

 return (
  <div style={{ marginTop: "30px" }}>
    <h3>Equipment Distribution</h3>

    <button
      onClick={exportChart}
      style={{ marginBottom: "15px" }}
    >
      📄 Export Chart
    </button>

    <div
      style={{
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        gap: "30px",
        alignItems: "center",
      }}
    >
      <div
        style={{
          background: dark ? "#1f1f1f" : "#fafafa",
          padding: "20px",
          borderRadius: "8px",
        }}
      >
        <h4 style={{ textAlign: "center" }}>Bar Chart</h4>
        <Bar data={data} />
      </div>

      <div
        style={{
          background: dark ? "#1f1f1f" : "#fafafa",
          padding: "20px",
          borderRadius: "8px",
        }}
      >
        <h4 style={{ textAlign: "center" }}>Pie Chart</h4>
        <Pie data={data} />
      </div>
    </div>
  </div>
);
}

export default Charts;