import { useState } from "react";
import UploadCSV from "./components/UploadCSV";

function App() {
  const [summary, setSummary] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Chemical Equipment Parameter Visualizer</h1>
      <p>Hybrid Web + Desktop Application</p>

      <UploadCSV onUploadSuccess={setSummary} />

      {summary && (
        <pre style={{ background: "#f4f4f4", padding: "10px" }}>
          {JSON.stringify(summary, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default App;