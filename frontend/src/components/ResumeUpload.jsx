//Handles client-side resume file selection and uploads it to the backend.
//Acts as the entry point for resume data into the AI analysis pipeline.

import { useState } from "react";
import api from "../api/client";

function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const uploadResume = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      await api.post("/upload-resume", formData);
      setStatus("✅ Resume uploaded successfully");
    } catch (err) {
      setStatus("❌ Upload failed");
    }
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <h3>Upload Resume</h3>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br />
      <button onClick={uploadResume} style={{ marginTop: "10px" }}>
        Upload
      </button>
      <p>{status}</p>
    </div>
  );
}

export default ResumeUpload;
