def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[-1] > blueShirtHeights[-1]:
        biggerArrayTrack = redShirtHeights
        smallerArrayTrack = blueShirtHeights
    else:
        biggerArrayTrack = blueShirtHeights
        smallerArrayTrack = redShirtHeights

    for i in range(len(biggerArrayTrack)):
        if (biggerArrayTrack[i] - smallerArrayTrack[i]) <= 0:
            return False
    return True
