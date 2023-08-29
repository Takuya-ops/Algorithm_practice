def minimumWaitingTime(queries):
    queries.sort()
    runningSum = prevTimes = 0

    for time in queries:
        runningSum += prevTimes
        prevTimes += time
    return runningSum
