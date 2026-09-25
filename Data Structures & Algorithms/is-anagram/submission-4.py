class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for i in s:
            if i not in dic_s:
                dic_s[i] = 1
            elif i in dic_s:
                dic_s[i] += 1
        for l in t:
            if l not in dic_t:
                dic_t[l] = 1
            elif l in dic_t:
                dic_t[l] += 1        
        if dic_s != dic_t:
            return False
        else:
            return True