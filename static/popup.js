(async () => {
  const res = await fetch('https://tiranga-smart-predictor.onrender.com/');
  const data = await res.json();
  alert(`Next color: ${data.likely_color} (${data.confidence}% confidence)`);
})();
