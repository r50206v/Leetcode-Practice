import math
class MachineEngine:
    
    def __init__(self):
        self.queue = []
        
    def add_order(self, order_id, volume):
        self.queue.append({'order_id': order_id, 'volume': volume, 'alloc': 0})
        
    def get_match(self, volume_to_match):
        ans = []
        
        first_alloc = math.ceil(volume_to_match * 0.4)
        second_alloc = volume_to_match - first_alloc
        for index in range(len(self.queue)):
            if first_alloc >= self.queue[index]['volume']:
                first_alloc -= self.queue[index]['volume']
                self.queue[index]['alloc'] = self.queue[index]['volume']
                self.queue[index]['volume'] = 0
            else:
                self.queue[index]['alloc'] = first_alloc
                self.queue[index]['volume'] -= first_alloc
                first_alloc = 0
                break
                
        percentage = {}
        total_order = 0
        for order in self.queue:
            percentage[order['order_id']] = order['volume']
            total_order += order['volume']
        
        if total_order == 0:
            return [(q['order_id'], q['alloc']) for q in self.queue]
        
        for order in self.queue:
            perc_alloc = round(second_alloc*percentage[order['order_id']]/total_order)
            ans.append((
                order['order_id'], 
                order['alloc'] + min(perc_alloc, order['volume'])
            ))
        return ans 


# 20 Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'{': '}', '[': ']', '<': '>', '(': ')'}

        if len(s) == 0:
            return True
        if len(s)%2 != 0:
            return False
        if s[0] in mapping.values():
            return False

        stack = []
        for p in s:
            if p in mapping.keys():
                stack.append(mapping[p])
            elif len(stack) != 0 and p == stack[-1]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


# 242 Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        if s_count == t_count:
            return True
        else:
            return False


# 125 Valid Palindrome
'''
Input: "A man, a plan, a canal: Panama"
Output: true
Input: "race a car"
Output: false
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
