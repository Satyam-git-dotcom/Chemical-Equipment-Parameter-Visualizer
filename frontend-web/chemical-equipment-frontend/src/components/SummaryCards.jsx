function SummaryCards({ summary }) {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))",
        gap: "15px",
        marginBottom: "30px",
      }}
    >
      <Card title="📦 Total Equipment" value={summary.total_equipment} />
      <Card title="🌊 Avg Flowrate" value={summary.avg_flowrate} />
      <Card title="⚙️ Avg Pressure" value={summary.avg_pressure} />
      <Card title="🌡️ Avg Temperature" value={summary.avg_temperature} />
    </div>
  );
}

function Card({ title, value }) {
  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "8px",
        padding: "20px",
        boxShadow: "0 2px 6px rgba(0,0,0,0.08)",
        textAlign: "center",
      }}
    >
      <h4 style={{ color: "#666", marginBottom: "8px" }}>{title}</h4>
      <div style={{ fontSize: "22px", fontWeight: "bold", color: "#4e73df" }}>
        {value}
      </div>
    </div>
  );
}

export default SummaryCards;