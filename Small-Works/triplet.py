class Triplet:

    def tripletCloseToTarget(self, arr, k):
        arr.sort()
        trip = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            findclosestPair(arr, k - arr[i], i + 1, trip)
        return trip
    
def findclosestPair(arr, targetSum, left, trip):
    right = len(arr) - 1
    