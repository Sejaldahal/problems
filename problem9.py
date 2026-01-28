# palindrome number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
           return False
        
  
        original = x
        reverse=0
        while x > 0:

            reverse=x%10 + reverse*10
            x=x//10
        return original == reverse
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    tests = [121, -121, 10, 12321, 0]

    for num in tests:
        result = solution.isPalindrome(num)
        print(f"{num} is palindrome: {result}")