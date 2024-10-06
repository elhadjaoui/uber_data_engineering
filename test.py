class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26
        # Count characters in s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        # Initialize the first window
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1
        if s1_count == window_count:
            return True
        print(s1_count)
        print(window_count)

        print('------------------------------------------------------')
        # Slide the window
        for i in range(len(s1), len(s2)):
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            window_count[ord(s2[i]) - ord('a')] += 1

            if s1_count == window_count:
                print(s1_count)
                print(window_count)
                return True
        print(s1_count)
        print(window_count)
        return False


s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))  # True
# print(s.checkInclusion("ab", "eidboaoo"))  # False
