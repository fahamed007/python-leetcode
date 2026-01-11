#https://leetcode.com/problems/keyboard-row/description/
#500. Keyboard Row
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row ="qwertyuiop"
        second_row="asdfghjkl"
        third_row="zxcvbnm"
        result=[]
        for word in words:
            lower_word=word.lower()
            first_char=lower_word[0]
            status=True
            if first_char in first_row:
                check=first_row
            elif first_char in second_row:
                check=second_row
            else:
                check=third_row
            for j in range(1, len(lower_word)):
                if lower_word[j] not in check:
                    status=False
                    break
            if status:
                result.append(word)
        return result
    
