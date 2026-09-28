class DutchFlag:
    def dutchSort(arr):
        left = 0
        right = len(arr) - 1
        i = 0
        while i <= right:
            if arr[i] == 0:
                arr[i], arr[left] = arr[left], arr[i]
                i += 1
                left += 1
            elif arr[i] == 1:
                i += 1
            else:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
        return arr
        
def main():
    arr = [1, 0, 2, 1, 0]
    print(DutchFlag.dutchSort(arr))
main()