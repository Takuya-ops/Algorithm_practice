def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    earlyBound = max(timeToMinutes(dailyBounds1[0]), timeToMinutes(dailyBounds2[0]))
    lateBound = min(timeToMinutes(dailyBounds1[1]), timeToMinutes(dailyBounds2[1]))

    freeTimeCalendar1 = getFreeTime(calendar1, earlyBound, lateBound)
    freeTimeCalendar2 = getFreeTime(calendar2, earlyBound, lateBound)

    overlapFreeTime = getCalendarOverlap(
        freeTimeCalendar1, freeTimeCalendar2, meetingDuration
    )
    return overlapFreeTime


def getCalendarOverlap(freeTimeCalendar1, freeTimeCalendar2, meetingDuration):
    timeOverlap = []
    for time1 in freeTimeCalendar1:
        for time2 in freeTimeCalendar2:
            if time1[0] < time2[1] and time1[1] > time2[0]:
                duration = min(time1[1], time2[1]) - max(time1[0], time2[0])
                if duration >= meetingDuration:
                    timeOverlap.append(
                        [
                            minutesToTime(max(time1[0], time2[0])),
                            minutesToTime(min(time1[1], time2[1])),
                        ]
                    )
    return timeOverlap


def getFreeTime(calendar, earlyBound, lateBound):
    freetime = []
    if calendar == []:
        return [[earlyBound, lateBound]]
    for idx in range(len(calendar)):
        startTime = timeToMinutes(calendar[idx][0])
        endTime = timeToMinutes(calendar[idx][1])
        prevEndTime = timeToMinutes(calendar[idx - 1][1])

        if idx == 0:
            if startTime > earlyBound:
                freetime.append([earlyBound, startTime])
        elif idx == len(calendar) - 1:
            if startTime > prevEndTime:
                freetime.append([prevEndTime, startTime])
            if endTime < lateBound:
                freetime.append([endTime, lateBound])
        else:
            if startTime > prevEndTime:
                freetime.append([prevEndTime, startTime])
    return freetime


def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes


def minutesToTime(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hoursStr = str(hours)
    minStr = str(mins) if mins > 0 else "00"
    return hoursStr + ":" + minStr
