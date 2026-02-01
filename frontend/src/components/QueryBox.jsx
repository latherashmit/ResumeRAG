//Accepts a user query and sends it along with the JD to the backend for AI analysis.
//Displays loading state and renders the AI-generated feedback.


import { useState } from "react";
import api from "../api/client";

function QueryBox({ jd }) {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const analyzeResume = async () => {
    setLoading(true);
    try {
      const res = await api.post("/analyze", null, {
        params: {
          query: query,
          jd: jd,
        },
      });
      setResponse(res.data.analysis);
    } catch (err) {
      setResponse("❌ Analysis failed");
    }
    setLoading(false);
  };

  return (
    <div>
      <h3>Ask a Question</h3>
      <input
        type="text"
        style={{ width: "100%", padding: "8px" }}
        placeholder="e.g. What skills am I missing?"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={analyzeResume} style={{ marginTop: "10px" }}>
        Analyze
      </button>

      {loading && <p>Analyzing...</p>}

      {response && (
        <div style={{ marginTop: "20px", whiteSpace: "pre-wrap" }}>
          <h4>AI Feedback</h4>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default QueryBox;
