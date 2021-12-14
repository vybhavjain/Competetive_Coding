class Solution:
    def balancedStringSplit(self, s: str) -> int:
        output = 0
        hashmap={'L':0 , 'R':0}
        for i in range(len(s)):
            hashmap[s[i]] += 1
            if hashmap['L'] == hashmap['R'] :
                hashmap['L'] = hashmap['R'] = 0
                output += 1
        return output