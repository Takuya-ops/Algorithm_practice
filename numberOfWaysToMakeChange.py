def numberOfWaysToMakeChange(n, demons):
    waysToMakeChange = [1] + [0 for _ in range(n)]
    for demon in demons:
        for change in range(demon, n + 1):
            waysToMakeChange[change] += waysToMakeChange[change - demon]
    return waysToMakeChange[-1]
