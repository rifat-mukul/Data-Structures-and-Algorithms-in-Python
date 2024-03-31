# You are given list of numbers, obtained by rotating a 
# sorted list an unknown number of times. Write a function 
# to determine the minimum number of times the original 
# sorted list was rotated to obtain the given list.
# Your function should have the worst-case complexity
# of O(log N), where N is the length of the list. 
# You can assume that all the numbers in the list are unique.


# Q: Express the problem in your own words below (to edit this cell, double click on it).

# Problem
#here a rotated sorted list that is roatted some unknown number 
# of times we need to find how many times it was rotated

# Q: The function you write will take one input called nums. What does it represent? Give an example.

# Input
# nums is a sorted rotated array  
# [6,7,3,4,5]

# Q: The function you write will return a single output called rotations. 
# What does it represent? Give an example.

# Output
# times of rotation 2
# 
# 

def compare(lo,hi,nums):
    if lo<hi:
        if nums[lo] > nums[lo+1]:
            return lo+1
        else:
            return compare (lo+1,hi,nums)
    return -1
def countRotaion(nums):
    lo = 0
    return compare(lo,len(nums)-1, nums)
# log(n)
# print(countRotaion([19,25,29,3,5,6,7,9,11,14]))

# now apply the efficient way to solve the problem
# that is binary search

# compare tme middle element with the last number 
# if the middle element is smaller than the last element the 
# answear lies on the first half of the array
# and if the middle element is smaller than the first element
# then the answear must be lies on the last half of the array 
# because we have to find the smalllest number
def countRotationBinary(nums):
    if len(nums)==1:
        return 0
    elif len(nums)==2:
        return 0 if nums[0] < nums[1] else 1
    lo=0
    hi=len(nums)-1
    while lo<=hi and len(nums) > 1:
        mid = (lo+hi)//2
        print(f"lo: {lo} hi: {hi} mid : {mid}")
        # min_val=nums[mid]
        if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
            return mid
        elif nums[mid] < nums[hi]:
            hi = mid-1
        elif nums[mid]>nums[hi]:  
            lo=mid+1
        else:
            return mid
    return 0
nums = [7,8,1,3,4,5,6]
# nums = [7,8,3,4,5]
# nums = [8,1]
# nums = []
print(countRotationBinary(nums))