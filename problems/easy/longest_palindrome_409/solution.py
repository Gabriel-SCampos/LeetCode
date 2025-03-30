class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters_count = {letter: s.count(letter) for letter in set(s)}

        has_impar_letter_occurrences = False
        output = 1
        for letter, count in letters_count.items():
            if count % 2 == 0:
                output += count
            else:
                output += count - 1
                has_impar_letter_occurrences = True

        if not has_impar_letter_occurrences:
            output -= 1
        return output

    def longestPalindrome_first_attempt(self, s):
        # this first version is not efficient, but it works
        """
        :type s: str
        :rtype: int
        """
        output = 0
        s_split = list(s)
        if not s_split:
            return output

        output += 1
        processed_letters = []
        has_impar_letter_occurrences = False
        for letter in s_split:
            if letter not in processed_letters: 
                letter_occurrences = s_split.count(letter)
                if (letter_occurrences % 2) == 0:
                    output += letter_occurrences
                else:
                    has_impar_letter_occurrences = True
                    output += (letter_occurrences - 1)
                processed_letters.append(letter)

        if not has_impar_letter_occurrences:
            output -= 1
        return output
