def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return "0s"
    
    hours = 0
    while totalSeconds >= 3600:
        hour += 1
        totalSeconds -= 3600
    
    minutes = 0
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60

    seconds = totalSeconds

    hms = []
    if hours > 0:
        hms.append(str(hours) + "h")
    if minutes > 0:
        hms.append(str(minutes) + "m")
    if seconds > 0:
        hms.append(str(seconds) + "s")

    return " ".join(hms)
