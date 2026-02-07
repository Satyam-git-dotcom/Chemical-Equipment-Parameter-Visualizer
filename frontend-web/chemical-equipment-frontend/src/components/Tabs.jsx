function Tabs({ activeTab, setActiveTab }) {
  const tabStyle = (tab) => ({
    padding: "10px 20px",
    cursor: "pointer",
    borderBottom: activeTab === tab ? "3px solid #4e73df" : "none",
    fontWeight: activeTab === tab ? "bold" : "normal",
  });

  return (
    <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
      <div style={tabStyle("analytics")} onClick={() => setActiveTab("analytics")}>
        📊 Analytics
      </div>
      <div style={tabStyle("history")} onClick={() => setActiveTab("history")}>
        🕒 History
      </div>
    </div>
  );
}

export default Tabs;