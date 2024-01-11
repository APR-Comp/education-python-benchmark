def sort_age(lst):
    lst.sort(key = lambda x: x[-2], reverse = True)
    return lst
