# ２つのカレンダーのスケジュールを比較し、共通の空き時間を見つける関数
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # 両カレンダーの営業開始と終了の最大・最小時間を取得
    earlyBound = max(timeToMinutes(dailyBounds1[0]), timeToMinutes(dailyBounds2[0]))
    lateBound = min(timeToMinutes(dailyBounds1[1]), timeToMinutes(dailyBounds2[1]))

    # それぞれのカレンダーから空き時間を抽出
    freeTimeCalendar1 = getFreeTime(calendar1, earlyBound, lateBound)
    freeTimeCalendar2 = getFreeTime(calendar2, earlyBound, lateBound)

    # ２つのカレンダーの空き時間を比較し、meetingDuration以上の重なる空き時間を見つける
    overlapFreeTime = getCalendarOverlap(
        freeTimeCalendar1, freeTimeCalendar2, meetingDuration
    )
    return overlapFreeTime


# ２つのカレンダーの空き時間を比較する関数。
def getCalendarOverlap(freeTimeCalendar1, freeTimeCalendar2, meetingDuration):
    timeOverlap = []
    for time1 in freeTimeCalendar1:
        for time2 in freeTimeCalendar2:
            # ２つの空き時間が重なっているかを判定
            if time1[0] < time2[1] and time1[1] > time2[0]:
                # 重なっている場合、重なりの時間を計算
                duration = min(time1[1], time2[1]) - max(time1[0], time2[0])
                # meetingDuration以上の重なる時間を抽出
                if duration >= meetingDuration:
                    timeOverlap.append(
                        [
                            minutesToTime(max(time1[0], time2[0])),
                            minutesToTime(min(time1[1], time2[1])),
                        ]
                    )
    return timeOverlap


# カレンダーから空き時間を抽出する関数
def getFreeTime(calendar, earlyBound, lateBound):
    freetime = []
    if calendar == []:
        return [[earlyBound, lateBound]]
    for idx in range(len(calendar)):
        startTime = timeToMinutes(calendar[idx][0])
        endTime = timeToMinutes(calendar[idx][1])
        prevEndTime = timeToMinutes(calendar[idx - 1][1]) if idx > 0 else earlyBound

        # 前の予定の終了と次の予定の開始の間の空き時間を抽出
        if startTime > prevEndTime:
            freetime.append([prevEndTime, startTime])

        # 最後の予定の後に空き時間がある場合、それを抽出
        if idx == len(calendar) - 1:
            if endTime < lateBound:
                freetime.append([endTime, lateBound])
    return freetime


# 時間を分に変換する関数
def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes


# 分を時間に変換する関数
def minutesToTime(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hoursStr = str(hours)
    minsStr = str(mins) if mins > 0 else "00"
    return hoursStr + ":" + minsStr


# テスト
if __name__ == "__main__":
    # 予定が埋まっている時間（Person1）
    calendar1 = [
        ["9:00", "10:30"],
        ["12:00", "13:00"],
        ["16:00", "18:00"],
    ]
    # 予定が踏まっている時間（Person2）
    calendar2 = [
        ["10:00", "11:30"],
        ["12:30", "14:30"],
        ["14:30", "15:00"],
        ["16:00", "17:00"],
    ]
    dailyBounds1 = ["9:00", "20:00"]
    dailyBounds2 = ["10:00", "18:30"]
    meetingDuration = 30
    print(
        calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )
    )
