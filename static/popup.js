**📁 File: `popup.js` (Neon UI Popup Frontend)**
```javascript
(function() {
    const style = document.createElement("style");
    style.textContent = `
        #tiranga-popup {
            position: fixed;
            top: 20px;
            right: 20px;
            width: 300px;
            background: #0f0f0f;
            border: 2px solid #0ff;
            color: #0ff;
            padding: 20px;
            font-family: monospace;
            font-size: 14px;
            z-index: 9999;
            box-shadow: 0 0 20px #0ff;
            border-radius: 10px;
        }
    `;
    document.head.appendChild(style);

    const popup = document.createElement("div");
    popup.id = "tiranga-popup";
    popup.innerHTML = "Loading prediction...";
    document.body.appendChild(popup);

    const fetchPrediction = async () => {
        const res = await fetch("https://tiranga-smart-predictor.onrender.com/api/predict");
        const data = await res.json();
        popup.innerHTML = `
            <strong>Prediction:</strong> ${data.color.toUpperCase()}<br>
            Confidence: ${data.confidence}%<br>
            Streak: ${data.streak}<br>
            Time: ${data.timestamp}
        `;
    };

    setInterval(fetchPrediction, 5000);
})();
```
