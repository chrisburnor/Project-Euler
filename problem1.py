# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# 
# Answer: 233168

# Pretty straigtforward.
# Loop over integers less than max. Then for each number,
# test if that integer is divisible by that number
def sumMultiples(max, multiplesList):
    sum = 0
    for i in range(1, max):
        for j in multiplesList:
            if (not (i % j)):
                sum += i
                break   # Once we've added it, break to avoid adding i multiple times if it is multiply multiple
    return sum    
    
if __name__ == "__main__":
    print sumMultiples(1000, [ 3, 5 ])
