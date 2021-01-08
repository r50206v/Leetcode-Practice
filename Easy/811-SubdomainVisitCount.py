''' 
time: O(N * max(k)) 
k is the length of subdomains

space: O(N)
'''
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        count = collections.defaultdict(int)
        for c in cpdomains:
            times, domains = c.split(" ")
            times = int(times)
            
            domainsList = domains.split(".")
            for idx in range(len(domainsList)):
                d = ".".join(domainsList[idx:])
                count[d] += times
            
        ans = []
        for k, v in count.items():
            ans.append(str(v) + " " + k)
        return ans
            

class Solution(object):
    def subdomainVisits(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in xrange(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]