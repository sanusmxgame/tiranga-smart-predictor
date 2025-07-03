
// ==UserScript==
// @name         Tiranga WebSocket Interceptor
// @namespace    http://tampermonkey.net/
// @version      1.2
// @description  Capture WebSocket game data and send to backend
// @match        https://tirangagame.top/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const BACKEND_URL = 'https://tiranga-smart-predictor.onrender.com/static/popup.js';
    const OriginalWebSocket = window.WebSocket;

    window.WebSocket = function(url, protocols) {
        const ws = protocols ? new OriginalWebSocket(url, protocols) : new OriginalWebSocket(url);
        const send = ws.send;

        ws.send = function(data) {
            return send.call(this, data);
        };

        ws.addEventListener('message', function(event) {
            try {
                const data = event.data;
                if (!data.includes('{')) return;

                const parsed = JSON.parse(data.slice(data.indexOf('{')));
                if (parsed.hash && parsed.round) {
                    fetch(BACKEND_URL, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            hash: parsed.hash,
                            round: parsed.round,
                            timestamp: Date.now()
                        })
                    });
                }
            } catch (e) {
                console.warn("Failed to parse WebSocket message:", e);
            }
        });

        return ws;
    };

    window.WebSocket.prototype = OriginalWebSocket.prototype;
})();
