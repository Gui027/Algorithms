def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for entrance, exit in permanence_period:
        if type(entrance) != int or type(exit) != int:
            return None

        if target_time >= entrance and target_time <= exit:
            count += 1

    return count
