'''
pairing the lightest person with the heaviest person
until it reach the boat limit, 
and then move on the next heaviest person

time: O(NlogN)
space: O(N)
'''
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans