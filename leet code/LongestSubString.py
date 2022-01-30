class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val = 0
        current_val = 0
        unique = []
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            if s[i] in unique:
                if max_val < current_val:
                    max_val = current_val
                    current_val = 1
                    unique = [s[i]]
            elif s[i] not in unique:
                unique.append(s[i])
                current_val = current_val + 1
        if max_val < current_val:
                    max_val = current_val
        return max_val