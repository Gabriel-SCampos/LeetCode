class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        last_number = -1
        for word in words:
            if word.isdigit():
                int_word = int(word)
                if int_word > last_number:
                    last_number = int(int_word)
                else:
                    return False
        return True