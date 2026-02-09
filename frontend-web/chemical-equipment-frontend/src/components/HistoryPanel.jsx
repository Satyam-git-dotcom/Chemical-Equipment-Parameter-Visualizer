import { useEffect, useState } from "react";
import api from "../services/api";

function HistoryPanel({ onSelect, refreshTrigger }) {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    api.get("history/").then((res) => setHistory(res.data));
  }, [refreshTrigger]);

  return (
    <div style={{ marginTop: "20px" }}>
      <h3 style={{ marginBottom: "16px" }}>Recent Upload History</h3>

      {history.length === 0 && (
        <p style={{ color: "#6b7280" }}>No datasets uploaded yet.</p>
      )}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr",
          gap: "14px",
        }}
      >
        {history.map((item) => (
          <div
            key={item.id}
            onClick={() => onSelect(item.summary)}
            style={{
              background: "#ffffff",
              borderRadius: "14px",
              padding: "16px 18px",
              boxShadow: "0 8px 20px rgba(0,0,0,0.06)",
              cursor: "pointer",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              flexWrap: "wrap",
              gap: "12px",
            }}
          >
            {/* Left info */}
            <div>
              <div style={{ fontWeight: "600", marginBottom: "4px" }}>
                Dataset #{item.id}
              </div>
              <div style={{ fontSize: "14px", color: "#6b7280" }}>
                Uploaded: {item.uploaded_at}
              </div>
              <div style={{ fontSize: "14px", color: "#6b7280" }}>
                Total Equipment: {item.summary.total_equipment}
              </div>
            </div>

            {/* Actions */}
            <div>
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  window.open(
                    `http://127.0.0.1:8000/api/pdf/${item.id}/`,
                    "_blank"
                  );
                }}
                style={{
                  padding: "8px 14px",
                  borderRadius: "8px",
                  border: "none",
                  cursor: "pointer",
                  background: "#2563eb",
                  color: "#ffffff",
                  fontWeight: "600",
                }}
              >
                📄 Download PDF
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default HistoryPanel;