# Tiranga Smart Predictor

## Features
- Fetches and decodes real-time results (30S, 1M, 3M, 5M).
- Uses WebSocket to track live data.
- Neon pop-up with live predictions on the game site.
- Predicts color, number, and size.
- Admin dashboard to view results.

## Deployment
1. Upload to Render
2. Ensure MongoDB connection string in `render.yaml`
3. Start both Flask server and WebSocket sniffer.
