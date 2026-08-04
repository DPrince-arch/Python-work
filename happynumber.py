def happyNumber(num):
    total = 0
    store = []
    while num > 0:
        if len(str(num)) == 1:
             total += num * num
        else:
            for digit in str(num):
                total += int(digit) ** 2
        if total != 1:
            if total in store:
                return False
            else:
                store.append(total)
                num = total
                total = 0
        else:
            return True
    
            

def main():
    print("Is 23 a happy number? " + str(happyNumber(23)))
    print("Is 12 a happy number? " + str(happyNumber(12)))

main()