class Minimum:
    @staticmethod

    def minSubArraySum(k, arr):
        window_sum = 0
        window_start = 0
        min_length = float('inf')
        sub = []

        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            while window_sum >= k:
                if window_end - window_start + 1 < min_length:
                    min_length = window_end - window_start + 1
                    sub = arr[window_start:window_end + 1]

                window_sum -= arr[window_start]
                window_start += 1

        return sub


def main():
    arr = [2, 3, 4, 1, 5]
    k = 6
    result = Minimum.minSubArraySum(k, arr)
    print("The smallest sub array that add up to", k, "are indexes ", result)


if __name__ == "__main__":
    main()
