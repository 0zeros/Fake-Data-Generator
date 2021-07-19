import random


# take number of digits as parameter
# calculate upper bound and lower bound in which numbers of specific digits lay
# pick a random number between those limits
def integer_of_length(number_of_digit):
    l_limit = 10**(number_of_digit-1)
    u_limit = 10**number_of_digit-1
    return random.randint(l_limit, u_limit)


# take lower and upper limit of range as parameters
# pick a random integer and return that
def integer_between(range_start, range_end):
    return random.randint(range_start, range_end)
