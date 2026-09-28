class Square:

    def squareOfNumber(arr, n):
        n = len(arr)
        squares = [n]
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(arr[left]) > abs(arr[right]):
                squares[i] = arr[left] * arr[left]
                left += 1
            else:
                squares[i] = arr[right] * arr[right]
                right -= 1
        return squares