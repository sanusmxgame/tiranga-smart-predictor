from database import get_history
import random

def predict_next_round():
    data = get_history()
    reds = sum(1 for d in data if d['color'] == 'Red')
    greens = sum(1 for d in data if d['color'] == 'Green')
    violets = sum(1 for d in data if d['color'] == 'Violet')
    total = reds + greens + violets

    def score(c): return round(100 * c / total, 2) if total else 0
    prediction = {
        "likely_color": max((('Red', reds), ('Green', greens), ('Violet', violets)), key=lambda x: x[1])[0],
        "confidence": score(max(reds, greens, violets)),
        "likely_range": "0-4" if random.random() > 0.5 else "5-9",
        "side": "Big" if random.random() > 0.5 else "Small"
    }
    return prediction
