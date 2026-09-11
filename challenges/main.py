def path_hits_blocked(blocked, path):
    for block in blocked:
        if block in path:
            return True
    return False 
    # TODO: check whether any position in `path` also appears in `blocked`
    pass