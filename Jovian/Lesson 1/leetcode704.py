
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        print(f"mid {mid} lo {lo} hi {hi}")
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        
    return -1

nums=[-1,0,3,5,9,12]
print(search(nums, 2))
