# QUESTION 1:
#  Alice has some cards with 
# numbers written on them. 
# She arranges the cards in 
# decreasing order, and lays them 
# out face down in a sequence on a table. 
# She challenges Bob to pick out the card containing a 
# given number by turning over as few cards as possible. 
# Write a function to help Bob locate the card.
# =====================================
# stpe 3
# =======
# We need to write a program to find the position of a 
# given number in a list of numbers arranged in 
# decreasing order. We also need to minimize the number
# of times we access elements from the list.
# ============================================
# this problem have 2 solution 
# brute force[linear search] 
# binary search
#============================================


# brute force[linear search]
def locate_card(cards, query):
    # create a position
    position = 0

    while position < len(cards):
        #assume the card is exist
        if cards[position] == query:

            #return the value
            return position
        
        #increment the position
        position += 1
        
        #check if the card is not exist
        if len(cards) == position:
            return "The card dose not exist"
    return "there is no card in given queue"
        

#text case
cards = []
query = 0

#call the function and print it
print(locate_card(cards, query))

# now analyze the solution and time complexity
# now binary search for the problem

def test_location(cards, query, mid):
    mid_val = cards[mid]
    print (f"mid {mid}, min_val: {mid_val}")
    if mid_val == query:
        if mid - 1 > 0 and mid_val == cards[mid - 1]:
            return "left"
        else:
            return "found"
    elif mid_val > query:
        return "right"
    else:
        return "left"


def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:            
        mid = (lo + hi) // 2
        print(f"lo : {lo} hi {hi}  mid {mid}")
        result = test_location(cards, query, mid)
        #check 
        if result == "left":
            hi = mid - 1      
        elif result == "right":
            lo = mid + 1
        else:
            return mid


# card = []  
cards = [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0]
query = 0
print(locate_card(cards, query))
