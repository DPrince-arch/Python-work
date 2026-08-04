class SmallSum:
    def tripWithSmallSum(arr, k):
        arr.sort()
        count = 0
        for i in range(len(arr) - 2):
            count += SmallSum.findPair(arr, k - arr[i], i)
        return count

    def findPair(arr, k, first):
        count = 0
        left = first + 1
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < k:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
    
def main():
    arr = [-1, 4, 2, 1, 3]
    k = 5
    print(SmallSum.tripWithSmallSum(arr, k))
main()