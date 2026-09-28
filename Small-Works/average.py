class Average:
    @staticmethod

    def findAverages(k, arr):
        averages = []
        windowSum = 0
        windowEnd = 0
        while windowEnd < len(arr):
            windowSum += arr[windowEnd]
            if windowEnd >= k - 1:
                averages.append(windowSum / k)
                windowSum -= arr[windowEnd - k + 1]
            windowEnd += 1    
        return averages

def main():
    k = 5
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    result = Average.findAverages(k, arr)
    print("Averages of subarrays of size " + str(k) + ": " + str(result))

if __name__ == "__main__":
    main()