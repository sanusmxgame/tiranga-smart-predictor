(function () {
    'use strict';
    const BACKEND_URL = 'https://tiranga-smart-predictor.onrender.com/api/results';

    const colorMap = {
        red: '#FF3B3F',
        green: '#00FF95',
        purple: '#B374FF'
    };

    function createPopup() {
        const popup = document.createElement('div');
        popup.id = 'tirangaPopup';
        popup.style.position = 'fixed';
        popup.style.top = '10px';
        popup.style.right = '10px';
        popup.style.zIndex = '99999';
        popup.style.background = '#111';
        popup.style.border = '2px solid #00FFFF';
        popup.style.borderRadius = '10px';
        popup.style.padding = '15px';
        popup.style.width = '280px';
        popup.style.color = '#fff';
        popup.style.fontFamily = 'monospace';
        popup.style.boxShadow = '0 0 20px #00FFFF';
        popup.innerHTML = `<h4 style="color:#00FFFF;text-align:center;">🎯 Smart Predictor</h4><div id="dataBlock">Loading...</div>`;
        document.body.appendChild(popup);
    }

    function updatePopup(data) {
        const block = document.getElementById('dataBlock');
        if (!block) return;

        let html = '';
        ['30S', '1M', '3M', '5M'].forEach(type => {
            const round = data[type]?.[0];
            if (round) {
                html += `
                    <div style="margin-top:10px">
                        <b style="color:#FFF">⏱ ${type}</b><br>
                        🧾 <b>Period:</b> ${round.period}<br>
                        🎲 <b>Number:</b> ${round.number}<br>
                        🖍 <b>Color:</b> <span style="color:${colorMap[round.color]}">${round.color}</span><br>
                        📏 <b>Size:</b> ${round.size}
                    </div>
                `;
            }
        });
        block.innerHTML = html;
    }

    async function fetchData() {
        try {
            const res = await fetch(BACKEND_URL);
            const json = await res.json();
            updatePopup(json);
        } catch (err) {
            console.error("Error fetching prediction:", err);
        }
    }

    function start() {
        createPopup();
        fetchData();
        setInterval(fetchData, 5000);
    }

    window.addEventListener('load', start);
})();
