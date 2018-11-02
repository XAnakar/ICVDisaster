
def ignored(substring, strings):

    for line in substring:
        if strings.lower().find(line.lower()) is not -1:
            return True
    return False
