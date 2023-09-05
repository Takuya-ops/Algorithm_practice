def stableInternships(interns, teams):
    matchings = {}
    available_interns = [True] * len(interns)

    while any(available_interns):
        for intern, is_available in enumerate(available_interns):
            if is_available:
                team = interns[intern][0]
                del interns[intern][0]

                if team not in matchings:
                    matchings[team] = intern
                    available_interns[intern] = False
                else:
                    current_intern = matchings[team]
                    if teams[team].index(intern) < teams[team].index(current_intern):
                        matchings[team] = intern
                        available_interns[intern] = False
                        available_interns[current_intern] = True

    return [[val, key] for key, val in matchings.items()]
