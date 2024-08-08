class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, no permutation of s1 can be a substring of s2
        if len(s1) > len(s2):
            return False

        # Initialize frequency dictionaries for characters 'a' to 'z'
        s1Freq = {chr(char): 0 for char in range(ord('a'), ord('z') + 1)}
        windowFreq = {chr(char): 0 for char in range(ord('a'), ord('z') + 1)}
        
        # Count the frequency of each character in s1 and the first window of s2
        for i in range(len(s1)):
            s1Freq[s1[i]] += 1
            windowFreq[s2[i]] += 1
        
        # Initialize the match count
        matches = 0
        for char in s1Freq:
            if s1Freq[char] == windowFreq[char]:
                matches += 1
        
        # If all 26 characters match, return True
        if matches == 26:
            return True
        
        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            startChar = s2[i - len(s1)]  # Character going out of the window
            endChar = s2[i]  # Character coming into the window

            # Add the new character to the current window
            if windowFreq[endChar] == s1Freq[endChar]:
                matches -= 1
            windowFreq[endChar] += 1
            if windowFreq[endChar] == s1Freq[endChar]:
                matches += 1
            
            # Remove the character that is no longer in the window
            if windowFreq[startChar] == s1Freq[startChar]:
                matches -= 1
            windowFreq[startChar] -= 1
            if windowFreq[startChar] == s1Freq[startChar]:
                matches += 1

            # Check if the current window matches s1
            if matches == 26:
                return True

        return False
