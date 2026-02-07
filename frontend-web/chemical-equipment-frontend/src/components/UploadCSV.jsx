import { useState } from "react";
import api from "../services/api";

function UploadCSV({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const response = await api.post("upload/", formData);
      onUploadSuccess(response.data);
    } catch (error) {
      alert("Upload failed");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        marginBottom: "30px",
        padding: "20px",
        border: "1px solid #e0e0e0",
        borderRadius: "8px",
        background: "#fafafa",
      }}
    >
      <h3>Upload Equipment CSV</h3>

      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload CSV"}
      </button>
    </div>
  );
}

export default UploadCSV;