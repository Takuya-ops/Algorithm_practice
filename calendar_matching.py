def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # 両者の開始時間のうち、より遅い方をearlyBoundに、終了時間のうち、より早い方をlateBoundに設定
    earlyBound = max(timeToMinutes(dailyBounds1[0]), timeToMinutes(dailyBounds2[0]))
    lateBound = min(timeToMinutes(dailyBounds1[1]), timeToMinutes(dailyBounds2[1]))

    # 各カレンダーの空き時間を取得
    freeTimeCalendar1 = getFreeTime(calendar1, earlyBound, lateBound)
    freeTimeCalendar2 = getFreeTime(calendar2, earlyBound, lateBound)

    # 両者の空き時間で、meetingDurationを満たす重なる時間帯を取得
    overlapFreeTime = getCalendarOverlap(
        freeTimeCalendar1, freeTimeCalendar2, meetingDuration
    )
    return overlapFreeTime


def getCalendarOverlap(freeTimeCalendar1, freeTimeCalendar2, meetingDuration):
    # 両者の空き時間のうち、meetingDurationを満たす重なる時間帯を取得
    timeOverlap = []
    for time1 in freeTimeCalendar1:
        for time2 in freeTimeCalendar2:
            if time1[0] < time2[1] and time1[1] > time2[0]:  # 時間帯が重なるかチェック
                duration = min(time1[1], time2[1]) - max(
                    time1[0], time2[0]
                )  # 重なる時間帯の長さを計算
                if duration >= meetingDuration:  # meetingDurationを満たす場合のみ追加
                    timeOverlap.append(
                        [
                            minutesToTime(max(time1[0], time2[0])),
                            minutesToTime(min(time1[1], time2[1])),
                        ]
                    )
    return timeOverlap


def getFreeTime(calendar, earlyBound, lateBound):
    # カレンダー内の空き時間を取得
    freetime = []
    if calendar == []:
        return [[earlyBound, lateBound]]  # カレンダーが空の場合は、earlyBoundからlateBoundまでが空き時間
    for idx in range(len(calendar)):
        startTime = timeToMinutes(calendar[idx][0])  # 開始時間を分に変換
        endTime = timeToMinutes(calendar[idx][1])  # 終了時間を分に変換
        prevEndTime = timeToMinutes(calendar[idx - 1][1])  # 前の予定の終了時間を分に変換

        if idx == 0:  # 最初の予定の場合
            if (
                startTime > earlyBound
            ):  # 最初の予定がearlyBoundよりも遅い場合は、earlyBoundからstartTimeまでが空き時間
                freetime.append([earlyBound, startTime])
        elif idx == len(calendar) - 1:  # 最後の予定の場合
            if (
                startTime > prevEndTime
            ):  # 前の予定の終了時間よりも開始時間が遅い場合は、前の予定の終了時間からstartTimeまでが空き時間
                freetime.append([prevEndTime, startTime])
            if endTime < lateBound:  # 終了時間がlateBoundよりも早い場合は、endTimeからlateBoundまでが空き時間
                freetime.append([endTime, lateBound])
        else:  # 最初でも最後でもない場合（中間の予定）
            if (
                startTime > prevEndTime
            ):  # 前の予定の終了時間よりも開始時間が遅い場合は、前の予定の終了時間からstartTimeまでが空き時間
                freetime.append([prevEndTime, startTime])
    return freetime


def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))  # "hh:mm"形式の時刻を時間と分に分割
    return hours * 60 + minutes  # 時間を分に変換して返す


def minutesToTime(minutes):
    hours = minutes // 60  # 分を時間に変換
    mins = minutes % 60  # 分を計算
    hoursStr = str(hours)
    minStr = str(mins) if mins > 0 else "00"  # 分が0の場合は'00'とする
    return hoursStr + ":" + minStr  # "hh:mm"形式の時刻文字列を返す
