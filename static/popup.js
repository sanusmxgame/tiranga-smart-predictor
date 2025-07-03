(async () => {
  const box = document.createElement("div");
  box.style.position = "fixed";
  box.style.bottom = "20px";
  box.style.right = "20px";
  box.style.background = "#111";
  box.style.border = "2px solid #e00";
  box.style.color = "#f55";
  box.style.fontSize = "16px";
  box.style.fontFamily = "monospace";
  box.style.padding = "10px";
  box.style.zIndex = 9999;
  box.innerText = "Loading prediction...";
  document.body.appendChild(box);

  try {
    const res = await fetch("https://tiranga-smart-predictor.onrender.com/static/popup.js");
    const data = await res.json();
    box.innerText = `🎯 ${data.likely_color}\nConfidence: ${data.confidence}%\nRange: ${data.likely_range}\nSide: ${data.side}`;
  } catch (e) {
    box.innerText = "Prediction failed";
  }
})();
