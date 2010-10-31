# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857

def maxpFactor(num):
    # The number in question is too large for range() so 
    # we loop over pure integers (C-like)
    # Start with i = 2 since 0 and 1 aren't prime
    i = 2;
    # The largest prime factor can't be more than half 
    # the value since 2 is the smallest prime factor 
    # it could be multiplied to get the number
    while i <= (num / 2):
        if not (num % i):
            print "%i is divisible by %i" % (num, i)
            # if it is divisible by i, divide i out and redo
            return maxpFactor(num / i)
        i += 1
    # if haven't returned anything by this point, 
    # num must be prime
    return num

if __name__ == "__main__":
    print maxpFactor(600851475143)
