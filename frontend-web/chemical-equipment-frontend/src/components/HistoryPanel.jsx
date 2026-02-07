import { useEffect, useState } from "react";
import api from "../services/api";

function HistoryPanel({ onSelect }) {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    api.get("history/").then(res => setHistory(res.data));
  }, []);

  return (
    <div style={{ marginTop: "30px" }}>
      <h3>Recent Upload History (Last 5)</h3>

      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th>Dataset</th>
            <th>Uploaded At</th>
            <th>Total</th>
            <th>PDF</th>
          </tr>
        </thead>
        <tbody>
          {history.map(item => (
            <tr
              key={item.id}
              style={{ cursor: "pointer" }}
              onClick={() => onSelect(item.summary)}
            >
              <td>{item.name}</td>
              <td>{item.uploaded_at}</td>
              <td>{item.summary.total_equipment}</td>
              <td>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    window.open(
                      `http://127.0.0.1:8000/api/report/${item.id}/`
                    );
                  }}
                >
                  📄 PDF
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default HistoryPanel;