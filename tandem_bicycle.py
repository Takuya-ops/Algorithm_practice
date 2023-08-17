def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)

    return sum(
        [max(redShirtSpeeds[i], blueShirtSpeeds[i]) for i in range(len(redShirtSpeeds))]
    )
