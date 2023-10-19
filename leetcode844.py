class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_result: str = ''
        t_result: str = ''
        for i in s:
            s_result = s_result[:-1] if i == '#' else s_result + i
        for i in t:
            t_result = t_result[:-1] if i == '#' else t_result + i
        return s_result == t_result


if __name__ == '__main__':
    print(Solution().backspaceCompare('#c', 'ad#c'))
