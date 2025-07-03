from database import get_history

def analyze_streaks():
    data = get_history()
    last_color = None
    streak = 0
    max_streak = {"color": None, "count": 0}
    for d in data:
        if d["color"] == last_color:
            streak += 1
        else:
            streak = 1
            last_color = d["color"]
        if streak > max_streak["count"]:
            max_streak = {"color": last_color, "count": streak}
    return max_streak
