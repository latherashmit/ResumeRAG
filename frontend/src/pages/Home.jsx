import ResumeUpload from "../components/ResumeUpload";
import JDInput from "../components/JDInput";
import QueryBox from "../components/QueryBox";
import { useState } from "react";

function Home() {
  const [jd, setJd] = useState("");

  return (
    <div style={{ maxWidth: "800px", margin: "40px auto", fontFamily: "Arial" }}>
      <h1>Resume RAG Reviewer</h1>

      <ResumeUpload />
      <JDInput jd={jd} setJd={setJd} />
      <QueryBox jd={jd} />
    </div>
  );
}

export default Home;
