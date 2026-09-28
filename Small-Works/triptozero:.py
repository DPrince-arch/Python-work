class Trips:
    def tripletToZero(self, arr):
        arr.sort()
        trip = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            findPair(arr, -arr[i], i + 1, trip)

        return trip

def findPair(arr, targetSum, left, trip):
    right = len(arr) - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            trip.append([-targetSum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1

def main():
    trip = Trips()
    print(trip.tripletToZero([-3, 0, 1, 2, -1, 1, -2]))

if __name__ == "__main__":
    main()