class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        bits = [len(bin(i)[2:].replace('0', '')) for i in arr]
        
        argmax = sorted(list(enumerate(bits)), key=lambda x: x[1])
        ans = []
        for idx, _ in argmax:
            ans.append(arr[idx])
        return ans


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # convert integers to bits
        arr = [bin(x)[2:] for x in arr]
        # sort the array based on string sort, then sort it based on 1's
        arr = sorted(sorted(arr), key = lambda x: (x.count('1'), len(x)))
        # convert them to integers and return as a list
        return [int(k, 2) for k in arr]