

class Challenge1:
    """
    Challenge 1.
    Something easy to warm up.
    There are N children standing in a line. Some of them may already have some candy.
    You are giving more candy to these children subjected to the following requirements:
            1. Each child must have at least one candy.
            2. Each child must have the same amount of candy.
    What is the minimum candy you must give?

    Example:
    Input: {3,2,1,0}, result: 6
    Input: {0,0,0},  result: 3
    """

    def countCandy(*candies):
        maxCandy, totalCandy  = 1 , 0
        for candy in candies:
            if candy>maxCandy: maxCandy = candy
            totalCandy+=candy
        return len(candies) * maxCandy - totalCandy

class Challenge2:
    """
    Exercise 2.
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. 
    Find the largest palindrome made from the product of two 3-digit numbers. Think how to optimize the algorithm.
    """
    
    def getLargestPalindrome(a, b):
        if len(str(a)+str(b))!= 6: raise NameError("arguments a: '" + str(a)  + "' and b: '" + str(b) + "', have to be 3-digit numbers!")
        for x in range(a,1,-1):
            for y in range(b, 1, -1):
                print(y)
            print (x)
  

def testing():
    print("Challenge1:")
    print (Challenge1.countCandy(3,2,1,0))
    print (Challenge1.countCandy(0,0,0))
    print("Challenge2:")
    print (Challenge2.getLargestPalindrome(110, 100))
    #print (getLargestPalindrome(999, 999))

if __name__ == "__main__":
    testing()
    