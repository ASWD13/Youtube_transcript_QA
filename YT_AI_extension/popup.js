document.getElementById("ask").addEventListener("click", async () => {
    const url = document.getElementById("url").value;
    const question = document.getElementById("question").value;
    const answerBox = document.getElementById("answer");
    const loadingText = document.getElementById("loading");
  
    answerBox.textContent = "";
    loadingText.style.display = "block";
  
    try {
      const res = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url, question })
      });
  
      const data = await res.json();
      answerBox.textContent = data.response || data.error || "No response.";
    } catch (err) {
      answerBox.textContent = "Error: " + err.message;
    } finally {
      loadingText.style.display = "none";
    }
  });
  