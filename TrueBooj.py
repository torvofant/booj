"""
TASK 
    Write a program that when given a range of numbers (for this test 1 to 75)
    that returns every number in the range. Keep in mind the following exceptions:
        -For multiples of 3, print "True".
        -For multiples of 5, print "Booj".
        -For multiples of 10, print "TrueBooj".
TEST
    from TrueBooj import truebooj
    print("\n".join(truebooj(x) for x in xrange(1, 75)))

DESIGN
    Looks like the test script expects truebooj to return a string because of
    the join method called
        Construct the return value as a string

ASSUMPTIONS
    1- Returning only one word if a number is divisible by more than one number
    like the number 30 is divisible by all three numbers. The order of checking
    for divisibility is 10, 5, 3

    2- Returning a list with one space between each number and word
"""


def testNum(num):
#Given a number, will return the number as a string or one of (TrueBooj,
#Booj, True)
    if num % 10 == 0:
        return "TrueBooj"
    elif num % 5 == 0:
        return "Booj"
    elif num % 3 ==0:
        return "True"
    else:
        return str(num)

def truebooj(number):
    ret_list = "" #string to create
    for i in range(1, number + 1): #+1 to include the number in the output
        ret_list += " " + testNum(i) #create string with space between
    return ret_list
