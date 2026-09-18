def has_conflict(meetings):
    for tuaka in range(len(meetings)):
        start1, end1 = meetings[tuaka]
        for praise in range(tuaka + 1, len(meetings)):
            start2, end2 = meetings[praise]
            if start1 < end2 and start2 < end1:
                return True
    return False            

    # TODO: return True if any two meetings overlap in time, False otherwise
    pass