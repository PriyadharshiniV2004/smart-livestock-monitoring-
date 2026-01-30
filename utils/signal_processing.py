def classify_activity(ax, ay, az):
    magnitude = abs(ax) + abs(ay) + abs(az)

    if magnitude < 0.2:
        return "Lying"
    elif magnitude < 0.5:
        return "Standing"
    else:
        return "Walking"

def classify_temperature(temp):
    if temp < 38.5:
        return "Normal"
    elif temp < 40.5:
        return "Low Fever"
    else:
        return "High Fever"

def classify_heart_rate(hr):
    if hr < 60 or hr > 90:
        return "Abnormal"
    return "Normal"
