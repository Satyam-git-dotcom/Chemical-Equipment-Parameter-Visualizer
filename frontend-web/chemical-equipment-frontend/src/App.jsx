import { useState } from "react";
import UploadCSV from "./components/UploadCSV";
import SummaryCards from "./components/SummaryCards";
import Charts from "./components/Charts";

function App() {
  const [summary, setSummary] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Chemical Equipment Parameter Visualizer</h1>
      <p>Hybrid Web + Desktop Application</p>

      <UploadCSV onUploadSuccess={setSummary} />

      {summary && (
        <>
          <SummaryCards summary={summary} />
          <Charts distribution={summary.equipment_distribution} />
        </>
      )}
    </div>
  );
}

export default App;