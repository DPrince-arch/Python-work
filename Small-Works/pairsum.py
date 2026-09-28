class PairSum:
    def pairSum(arr, k):
        left = 0
        right = len(arr) - 1
        sub = []
        while left < right:
            currentSum = arr[left] + arr[right]
            if currentSum == k:
                sub.append(arr[left], arr[right])
            elif currentSum < k:
                left += 1
                continue
            else:
                right -= 1
                continue
        return sub

def main():
    arr = [2, 3, 4, 1, 5]
    k = 6
    result = PairSum.pairSum(arr, k)
    print("The indexes that add up to " + str(k) + " are " + str(result))

if __name__ == "__main__":
    main()    