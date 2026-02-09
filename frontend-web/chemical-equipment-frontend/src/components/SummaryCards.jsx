function SummaryCards({ summary }) {
  return (
    <div style={gridStyle}>
      <Card
        title="Total Equipment"
        value={summary.total_equipment}
        color="#2563eb"
        icon="📦"
      />
      <Card
        title="Avg Flowrate"
        value={summary.avg_flowrate}
        color="#059669"
        icon="🌊"
      />
      <Card
        title="Avg Pressure"
        value={summary.avg_pressure}
        color="#7c3aed"
        icon="⚙️"
      />
      <Card
        title="Avg Temperature"
        value={summary.avg_temperature}
        color="#dc2626"
        icon="🌡️"
      />
    </div>
  );
}

function Card({ title, value, color, icon }) {
  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "14px",
        padding: "22px",
        boxShadow: "0 10px 25px rgba(0,0,0,0.06)",
        transition: "transform 0.2s ease, box-shadow 0.2s ease",
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.transform = "translateY(-4px)";
        e.currentTarget.style.boxShadow =
          "0 16px 35px rgba(0,0,0,0.1)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.transform = "translateY(0)";
        e.currentTarget.style.boxShadow =
          "0 10px 25px rgba(0,0,0,0.06)";
      }}
    >
      <div
        style={{
          fontSize: "28px",
          marginBottom: "10px",
        }}
      >
        {icon}
      </div>

      <div
        style={{
          fontSize: "14px",
          color: "#6b7280",
          marginBottom: "6px",
        }}
      >
        {title}
      </div>

      <div
        style={{
          fontSize: "26px",
          fontWeight: "700",
          color: color,
        }}
      >
        {value}
      </div>
    </div>
  );
}

const gridStyle = {
  display: "grid",
  gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
  gap: "20px",
  marginBottom: "32px",
};

export default SummaryCards;