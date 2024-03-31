# the queue is in the decreasing order


def BinarySearch(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi=mid-1
        else:
            lo=mid-1
    return -1

def locate_card(cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    return BinarySearch(0, len(cards)-1, condition)

cards = [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0]
query = 0
print(locate_card(cards, query))
