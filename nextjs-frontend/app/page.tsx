"use client";

import { useState } from "react";

interface PredictionResult {
  denied: boolean;
  probability: number;
}

export default function Home() {
  const [input, setInput] = useState({
    coding_acc: 0.85,
    payer_score: 0.75,
    amount: 0.6,
    prior_auth: 1,
    doc_quality: 0.9,
  });
  const [result, setResult] = useState<PredictionResult | null>(null);

  const handleSubmit = async () => {
    const res = await fetch("http://localhost:8000/predict-denial/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <div>
      <h1>RCM Denial Predictor</h1>
      <input
        type="number"
        value={input.coding_acc}
        onChange={(e) => setInput({ ...input, coding_acc: +e.target.value })}
        placeholder="Coding Accuracy"
      />
      {/* Add other inputs similarly */}
      <button onClick={handleSubmit}>Predict</button>
      {result && <p>Denied: {result.denied.toString()}, Probability: {result.probability.toFixed(2)}</p>}
    </div>
  );
}
