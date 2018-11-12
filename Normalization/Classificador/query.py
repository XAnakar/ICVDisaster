import bisect


def bs(sorted_collection, item):

    for line in sorted_collection:
        if item == line:
            return True
    return False


def mainz(base, query):

    for line in query:
        if bs(base, line.lower()):
            return True
    return False

