class MaxFruits:
    def maxFruits(self, fruits, k):
        windowStart = 0
        maxLength = 0
        fruitCount = {}

        for windowEnd in range(len(fruits)):
            right_fruit = fruits[windowEnd]
            if right_fruit not in fruitCount:
                fruitCount[right_fruit] = 0
            fruitCount[right_fruit] += 1

            while len(fruitCount) > k:
                left_fruit = fruits[windowStart]
                fruitCount[left_fruit] -= 1
                if fruitCount[left_fruit] == 0:
                    del fruitCount[left_fruit]
                windowStart += 1

            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength   
    
def main():
    fruits = ['A', 'B', 'C', 'A', 'C']
    k = 2
    max_fruits = MaxFruits()
    result = max_fruits.maxFruits(fruits, k)
    print("The maximum number of fruits that can be collected in two baskets is:", result)

if __name__ == "__main__":
    main()