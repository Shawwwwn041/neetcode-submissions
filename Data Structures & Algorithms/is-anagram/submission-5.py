class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sor_s = sorted(s)
        sor_t = sorted(t)
        if sor_s == sor_t:
            return True
        else:
            return False