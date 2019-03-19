
def ignored(substring, profile):

    for line in substring:
        if profile.lower().find(line.lower()) is not -1:
            return True
    return False