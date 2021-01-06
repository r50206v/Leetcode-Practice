class ListNode(object):
    def __init__(self, val=0):
        self.val = 0
        self.next = None
        self.parent = None


class Solution(object):
    
    def findInOrderSuccessor(input: ListNode):

        if not input:
            return None

        if input.right:
            return self.getMostLeft(input.right)

        parent = input.parent # 12
        child = input # 14

        while (parent.right == child):
            if not parent.parent:
                return None

            child = parent # 9
            parent = parent.parent # 20
 
        return parent
        # if node.right exists
            # go down to the right
            # and check if left exists
                # if it exists, go all the way left until null

        # else go up
            # go to the parent 
            # check which side you come from 
            # if left side, return parent
            # if right side, go up again
        
        
    def getMostLeft(x: ListNode):
        if x.left:
            # if left exists, go all the way left until null
            return self.getMostLeft(x.left)
        else:
            # if left null, then return x itself
            return x





def getShortestUniqueSubstring(chars, string):

    n = len(string)
    dist_count = len(chars)

    curr_count = collections.defaultdict(0)
    count = 0
    start = 0
    min_length = n

    for j in range(n):

        curr_count[string[j]] += 1

        if curr_count[string[j]] == 1:
            count += 1
        
        if count == dist_count:
            while curr_count[string[start]] > 1:
                if curr_count[string[start]] > 1:
                    curr_count[string[start]] -= 1
                start += 1

            len_window = j - start + 1

            if min_length > len_window:
                min_length = len_window
                start_index = start
    
    return str(string[start_index: start_index + min_length])
        

class Solution:

    def findNeedle(self, haystack, needle):
        ans = []

        if len(haystack) == 0 or len(needle) == 0:
            return ans
        if len(haystack) < len(needle):
            return ans
        
        i = 0
        while i >= 0:

            i = haystack[i:].index(needle)
            if i >= 0:
                ans.append(i)
                i += 1
        return ans




class Solution:
    def decodeString(self, s: str) -> str:
        # instantiate stacks to store the number and the string to repeat.
        repeatStr = []
        numRepeat = []
        
        # initialize empty strings. One to store a multidigit number and other one to store the decoded string. 
        tempNum = ''
        decodedStr = ''        
        
        # start iterating throught the encoded string
        for char in s:
            # check if the char is a digit. 
            if char.isdigit():
                tempNum += char # add the number to tempNum
                
            # check if the char is an opening bracket
            elif char == '[':
                repeatStr.append(decodedStr)
                numRepeat.append(tempNum)
                tempNum = ''
                decodedStr = ''
                
            # check when the bracket closes
            elif char == ']':
                decodedStr = repeatStr.pop() + (decodedStr * int(numRepeat.pop()))
                
            # else build the substring to repeat
            else:
                decodedStr += char            
                
        return decodedStr
# class Solution:
#     def decodeString(self, s: str) -> str:
        
#         result = ""
#         strStack = []
#         countStack = []
#         base = ""
        
#         for index in range(len(s)):
            
#             if s[index].isdigit():
#                 base += s[index]
            
#             elif s[index] == '[':
#                 strStack.append(result)
#                 result = ""
                
#                 countStack.append(int(base))
#                 base = ""
                
#             elif s[index] == ']':
#                 result = strStack.pop() * countStack.pop()
            
#             else:
#                 result += s[index]
                
#         return result