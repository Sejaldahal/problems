# longest substring without repeating characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset=set()
        left =0
        maxlength=0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left +=1

            charset.add(s[right])    
            maxlength=max(maxlength , right-left+1)
        return maxlength 
    
if __name__ == "__main__":
    s="abcabcbb"
    result=Solution().lengthOfLongestSubstring(s)
    print(result)    

#so here what exactly happens isin the class solution we have a function lengthoflongestsubstring which takes a string s as input
#we send an charset which is intially empty and weconsider two pointers left and right both starting at 0
# firstly we iterate right pointer when s [right ] is already in charset then we remove the char from s left and increment s left and again check for the next char 
# when s[right] is not in charset we add it to charset and update maxlength by calculating the maximum of current maxlength and the length of current substring (right - left + 1)
# finally we return maxlength which is the length of longest substring without repeating characters