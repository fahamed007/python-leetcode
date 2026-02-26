#https://leetcode.com/problems/reverse-words-in-a-string-iii/
#557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        l1=s.split()
        reversed_string=''
        for word in l1:
            reversed_string +=word[::-1] +" "
        return reversed_string.strip()
    
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseString(word):
            left=0
            right=len(word) -1
            new_words=[x for x in word]
            while left <right:
                new_words[left],new_words[right] = new_words[right],new_words[left]
                left +=1
                right -=1
            return "".join(new_words)
        
        s_list=s.split()
        new_s=[]
        for word in s_list:
            reverse_word =reverseString(word)
            new_s.append(reverse_word)
        return " ".join(new_s)
        
