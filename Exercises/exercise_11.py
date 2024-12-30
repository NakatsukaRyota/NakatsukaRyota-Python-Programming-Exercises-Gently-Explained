def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return "0s"

    date = []
    second = totalSeconds % 60
    totalMinutes = totalSeconds // 60
    minute = totalMinutes % 60
    totalHours = totalMinutes // 60
    hour = totalHours


    if hour != 0:
        date.append(str(hour) + "h")
    if minute != 0:
        date.append(str(minute) + "m")
    if second != 0:
        date.append(str(second) + "s")
    return(" ".join(date))

assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'