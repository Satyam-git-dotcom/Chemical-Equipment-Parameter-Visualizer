function SummaryCards({ summary }) {
  return (
    <div style={{ display: "flex", gap: "15px", marginBottom: "20px" }}>
      <Card title="Total Equipment" value={summary.total_equipment} />
      <Card title="Avg Flowrate" value={summary.avg_flowrate} />
      <Card title="Avg Pressure" value={summary.avg_pressure} />
      <Card title="Avg Temperature" value={summary.avg_temperature} />
    </div>
  );
}

function Card({ title, value }) {
  return (
    <div style={{
      padding: "15px",
      border: "1px solid #ddd",
      borderRadius: "8px",
      minWidth: "150px",
      textAlign: "center",
      background: "#f9f9f9",
    }}>
      <h3>{title}</h3>
      <p style={{ fontSize: "20px", fontWeight: "bold" }}>{value}</p>
    </div>
  );
}

export default SummaryCards;