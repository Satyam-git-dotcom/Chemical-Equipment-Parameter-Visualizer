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
        background: dark ? "#1e1e1e" : "#f4f6f8",
        color: dark ? "#ffffff" : "#000000",
        minHeight: "100vh",
        padding: "40px",
      }}
    >
      <div
        style={{
          maxWidth: "1100px",
          margin: "0 auto",
          background: dark ? "#2a2a2a" : "#ffffff",
          padding: "30px",
          borderRadius: "10px",
          boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
        }}
      >
        <button
          onClick={() => setDark(!dark)}
          style={{ float: "right", marginBottom: "10px" }}
        >
          {dark ? "☀️ Light Mode" : "🌙 Dark Mode"}
        </button>

        <h1>Chemical Equipment Parameter Visualizer</h1>
        <p style={{ color: dark ? "#ccc" : "#666", marginBottom: "25px" }}>
          Hybrid Web + Desktop Analytics Dashboard
        </p>

        <UploadCSV onUploadSuccess={handleUploadSuccess} />

        <Tabs activeTab={activeTab} setActiveTab={setActiveTab} />

        {activeTab === "analytics" && summary && (
          <>
            <SummaryCards summary={summary} />
            <Charts
              distribution={summary.equipment_distribution}
              dark={dark}
            />
            <LineChart summary={summary} dark={dark} />
          </>
        )}

        {activeTab === "history" && (
          <HistoryPanel
            refreshTrigger={refreshHistory}
            onSelect={setSummary}
          />
        )}
      </div>
    </div>
  );
}

export default App;