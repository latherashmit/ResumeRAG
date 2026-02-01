//Collects the job description text from the user via a controlled textarea.
//Pushes JD data upward to parent state for later analysis.

function JDInput({ jd, setJd }) {
  return (
    <div style={{ marginBottom: "20px" }}>
      <h3>Job Description</h3>
      <textarea
        rows="6"
        style={{ width: "100%" }}
        placeholder="Paste job description here..."
        value={jd}
        onChange={(e) => setJd(e.target.value)}
      />
    </div>
  );
}

export default JDInput;
