class Maximum:
    
    def maxSumArray(k, arr):
        sum = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == k:
                    sum.append((i, j))
        return sum

def main():
    arr = [2, 3, 4, 1, 5]
    k = 6
    result = Maximum.maxSumArray(k, arr)
    print("The indexes that add up to " + str(k) + " are " + str(result))

if __name__ == "__main__":
    main()