def loop_exists(arr: list[int]) -> bool:
    if not arr or len(arr) <= 1:
        return False

    for i in range(len(arr)):
        is_forward = arr[i] >= 0 
        slow, fast = i, i

        while True:
            slow = find_next_index(arr, is_forward, slow)
            fast = find_next_index(arr, is_forward, fast)
            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)

            if slow == -1 or fast == -1:
                break

            if slow == fast:
                return True

    return False

def find_next_index(arr: list[int], is_forward: bool, current_index: int) -> int:
    current_direction = arr[current_index] >= 0

    if is_forward != current_direction:
        return -1

    next_index = (current_index + arr[current_index]) % len(arr)

    if next_index == current_index:
        return -1

    return next_index


if __name__ == "__main__":
    print(loop_exists([1, 2, -1, 2, 2]))
    print(loop_exists([2, 2, -1, 2])) 
    print(loop_exists([2, 1, -1, -2]))



#gien_name = 567

#if food > 0 return  true
#  var name string = "Ade"
# 
# import {mee} from "./mee"
# contract mee { unit256 userBalance = 100}
# uint
# address
# enum
# struct
# bytes32 public name 
# string public name = "Ade"


#  from mee import find_next_index
# import mee

# export

# available_food = "rice"
# available_food = []string{"rice", "beans", "yam"}