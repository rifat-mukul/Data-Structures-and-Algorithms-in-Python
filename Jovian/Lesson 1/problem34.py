#34. Find First and Last Position of Element in Sorted Array
def binarysearch(lo, hi, condition):
    while lo<=hi:
        mid=(lo+hi) // 2
        result=condition(mid)
        if result=='found':
            return mid
        elif result =="left":
            hi=mid-1
        elif result=='right':
            lo=mid+1
    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid]==target:
            if mid>0 and nums[mid-1]==target:
                return "left"
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return "left"
    return binarysearch(0, len(nums)-1,condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid]==target:
            if mid>0 and nums[mid+1]==target:
                return "right"
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return "left"
    return binarysearch(0, len(nums)-1,condition)

def first_last_position(nums,target):
    return first_position(nums,target),last_position(nums,target)

nums = [5,7,7,8,9,10]
target = 8
print(first_last_position(nums,target))
#same problem with brote force solution
def firstposition(lo, hi, idx,arr):
    while lo>=hi:
        if arr[lo]==idx:
            return lo
        lo+=1

def lastposition(hi,lo,idx,ln,arr):
    while hi<=lo:
        if arr[hi]==idx:
            return (ln-hi)
        hi-=1

def first_last(arr,idx):
    return first_position(0,len(arr)-1, idx,arr),last_position(len(arr)-1, 0,idx,len(arr),arr)

arr =[5,7,7,8,9,10]
idx=8
print(first_last_position(arr,idx))