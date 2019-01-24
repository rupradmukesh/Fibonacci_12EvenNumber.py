def test_suite():
    for tst, exp in test_inputs.items():
        actual = check_palindrome(tst)
        # print (actual)
        if actual == True:
            print("OK")
        else:
            print("NOK")

def check_palindrome(string):
    """
        This checks if the given input string is a palindrome
        It returns True if the input string is a palindrome
        It returns False if the input string is not a palindrome
    """
    # Your code goes here
    reverse = string[::-1]
    # print( reverse )
    if ( reverse == string):
        return True # to indicate that the input string is a palindrome
    else:
        return False
# Main test cases
test_inputs = \
    {
        "radar" : True, # test string : expected status
        "panama" : False,
        "Madman" : False,
        "TCATGAACGTCTTCTGCAAGTACT" : True,
        "GACATACTCCTCCACCTCATACAG" : False,
    }


test_suite()
