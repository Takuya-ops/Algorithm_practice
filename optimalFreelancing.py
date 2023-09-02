def optimalFreelancing(jobs):
    if len(jobs) < 1:
        return 0
    maxPay = 0
    numDays = 7
    while numDays > 0:
        todaysMaxPay = 0
        idxToRemove = None
        for idx, job in enumerate(jobs):
            if job["deadline"] >= numDays:
                if job["payment"] > todaysMaxPay:
                    todaysMaxPay = job["payment"]
                    idxToRemove = idx
        if idxToRemove is not None:
            jobs.pop(idxToRemove)
            maxPay += todaysMaxPay
        numDays -= 1
    return maxPay
