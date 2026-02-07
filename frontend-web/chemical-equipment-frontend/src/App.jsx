import { useState } from "react";
import UploadCSV from "./components/UploadCSV";
import SummaryCards from "./components/SummaryCards";
import Charts from "./components/Charts";

function App() {
  const [summary, setSummary] = useState(null);

  return (
    <div style={{ padding: "40px" }}>
      <div
        style={{
          maxWidth: "1000px",
          margin: "0 auto",
          background: "#ffffff",
          padding: "30px",
          borderRadius: "10px",
          boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
        }}
      >
        <h1>Chemical Equipment Parameter Visualizer</h1>
        <p style={{ color: "#666", marginBottom: "25px" }}>
          Hybrid Web + Desktop Analytics Application
        </p>

        <UploadCSV onUploadSuccess={setSummary} />

        {summary && (
          <>
            <SummaryCards summary={summary} />
            <Charts distribution={summary.equipment_distribution} />
          </>
        )}
      </div>
    </div>
  );
}

export default App;