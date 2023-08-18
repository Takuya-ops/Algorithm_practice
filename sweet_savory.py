def sweetAndSavory(dishes, target):
    res = [0, 0]
    dishes.sort()
    l = 0
    r = len(dishes) - 1
    close = float("inf")
    while l < r and dishes[l] < 0 and dishes[r] > 0:
        cur = dishes[l] + dishes[r]
        if cur > target:
            r -= 1
            continue
        dif = target - cur
        if dif <= close:
            res[0] = dishes[l]
            res[1] = dishes[r]
            close = dif
        l += 1
    res.sort()
    return res
