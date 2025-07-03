(async () => {
  const res = await fetch('https://your-deployment-url/api/predict');
  const data = await res.json();
  alert(`Next color: ${data.likely_color} (${data.confidence}% confidence)`);
})();
