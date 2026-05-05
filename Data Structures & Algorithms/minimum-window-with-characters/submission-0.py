from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        if len(t) == 1 and t in s:
            return t
        t_values = defaultdict(int)
        window_size = 0
        for t_ch in t:
            t_values[t_ch] += 1
            window_size += 1

        def is_valid_window(t_d, s_d) -> bool:
            for ch, count in t_d.items():
                if s_d[ch] < count:
                    return False
            return True

        s_values = defaultdict(int)
        left = 0
        min_window = float("infinity")
        min_str = ""
        for right in range(0, len(s)):
            s_values[s[right]] += 1
            while left < right and is_valid_window(t_values, s_values):
                # print("t_values: ", t_values)
                # print("s_values: ", s_values)
                # print(f"Viewed str: {s[left:(right+1)]}")
                if (right - left + 1) < min_window:
                    min_str = s[left:(right + 1)]
                    min_window = right - left + 1
                s_values[s[left]] -= 1
                left += 1
                # print()

        return min_str