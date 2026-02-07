import { useState } from "react";
import UploadCSV from "./components/UploadCSV";
import SummaryCards from "./components/SummaryCards";
import Charts from "./components/Charts";
import HistoryPanel from "./components/HistoryPanel";

function App() {
  const [summary, setSummary] = useState(null);
  const [refreshHistory, setRefreshHistory] = useState(0);

  const handleUploadSuccess = (data) => {
    setSummary(data);
    setRefreshHistory((prev) => prev + 1);
  };

  return (
    <div style={{ padding: "40px" }}>
      <div
        style={{
          maxWidth: "1100px",
          margin: "0 auto",
          background: "#ffffff",
          padding: "30px",
          borderRadius: "10px",
          boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
        }}
      >
        <h1>Chemical Equipment Parameter Visualizer</h1>
        <p style={{ color: "#666", marginBottom: "25px" }}>
          Hybrid Web + Desktop Analytics Dashboard
        </p>

        <UploadCSV onUploadSuccess={handleUploadSuccess} />

        {summary && (
          <>
            <SummaryCards summary={summary} />
            <Charts distribution={summary.equipment_distribution} />
          </>
        )}

        <HistoryPanel refreshTrigger={refreshHistory} />
      </div>
    </div>
  );
}

export default App;