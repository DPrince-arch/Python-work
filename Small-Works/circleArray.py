from itertools import cycle

def circularArray(arr):
    arr = cycle(arr)
    if not arr:
        return False
    
    slow = arr[0]
    next = 0 + slow
    move = arr[next]

def main():
    arr = [1, 2, -1, 2, 2]
    print("Circular array has loop: " + str(circularArray(arr)))

main()   