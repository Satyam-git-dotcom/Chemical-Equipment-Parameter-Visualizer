import { useState } from "react";
import UploadCSV from "./components/UploadCSV";
import SummaryCards from "./components/SummaryCards";
import Charts from "./components/Charts";
import HistoryPanel from "./components/HistoryPanel";
import Tabs from "./components/Tabs";
import LineChart from "./components/LineChart";

function App() {
  const [dark, setDark] = useState(false);
  const [summary, setSummary] = useState(null);
  const [refreshHistory, setRefreshHistory] = useState(0);
  const [activeTab, setActiveTab] = useState("analytics");

  const handleUploadSuccess = (data) => {
    setSummary(data);
    setRefreshHistory((prev) => prev + 1);
    setActiveTab("analytics");
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        background: dark
          ? "linear-gradient(135deg, #1f2933, #111827)"
          : "linear-gradient(135deg, #f8fafc, #eef2ff)",
        padding: "40px 20px",
        transition: "all 0.3s ease",
      }}
    >
      <div
        style={{
          maxWidth: "1200px",
          margin: "0 auto",
          background: dark ? "#1f2937" : "#ffffff",
          borderRadius: "16px",
          padding: "32px",
          boxShadow: "0 15px 40px rgba(0,0,0,0.08)",
        }}
      >
        {/* Header */}
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            flexWrap: "wrap",
            gap: "16px",
            marginBottom: "24px",
          }}
        >
          <div>
            <h1 style={{ margin: 0 }}>
              Chemical Equipment Parameter Visualizer
            </h1>
            <p
              style={{
                marginTop: "6px",
                color: dark ? "#9ca3af" : "#6b7280",
              }}
            >
              Hybrid Web + Desktop Analytics Dashboard
            </p>
          </div>

          <button
            onClick={() => setDark(!dark)}
            style={{
              padding: "10px 16px",
              borderRadius: "10px",
              border: "none",
              cursor: "pointer",
              background: dark ? "#374151" : "#eef2ff",
              color: dark ? "#ffffff" : "#1e3a8a",
              fontWeight: "600",
            }}
          >
            {dark ? "☀️ Light Mode" : "🌙 Dark Mode"}
          </button>
        </div>

        {/* Upload */}
        <UploadCSV onUploadSuccess={handleUploadSuccess} />

        {/* Tabs */}
        <div style={{ marginTop: "30px" }}>
          <Tabs activeTab={activeTab} setActiveTab={setActiveTab} />
        </div>

        {/* Analytics */}
        {activeTab === "analytics" && summary && (
          <div style={{ marginTop: "30px" }}>
            <SummaryCards summary={summary} />
            <Charts
              distribution={summary.equipment_distribution}
              dark={dark}
            />
            <LineChart summary={summary} dark={dark} />
          </div>
        )}

        {/* History */}
        {activeTab === "history" && (
          <div style={{ marginTop: "30px" }}>
            <HistoryPanel
              refreshTrigger={refreshHistory}
              onSelect={setSummary}
            />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;