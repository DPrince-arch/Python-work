class removeDuplicate:
    def removeDups(arr):
        next = 1
        i = 1
        while i < len(arr):
            if arr[next - 1] != arr[i]:
                arr[next] = arr[i]
                next += 1
            i += 1
        return next
    
def main():
    arr = [1, 2, 2, 3, 4, 4, 5]
    result = removeDuplicate.removeDups(arr)
    print("The array after removing duplicates is: " + str(result))

if __name__ == "__main__": 
    main()