#https://leetcode.com/problems/add-strings/description/
#415. Add Strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans =[]
        ind_num1=len(num1) -1
        ind_num2=len(num2) -1
        carry=0
        while ind_num1 >=0 or ind_num2>=0:
            if ind_num1 >=0 and ind_num2>=0:
                sum_val= int(num1[ind_num1]) +int(num2[ind_num2]) +carry
                if sum_val >9:
                    ans.append(str(sum_val)[-1])
                    carry=1
                else: 
                    ans.append(str(sum_val)[0])
                    carry=0
                ind_num1 -=1
                ind_num2-=1
                    
            elif ind_num1 >=0:
                sum_val= int(num1[ind_num1]) + +carry
                if sum_val >9:
                    ans.append(str(sum_val)[-1])
                    carry=1
                else: 
                    ans.append(str(sum_val)[0])
                    carry=0
                ind_num1 -=1
            
            elif ind_num2 >=0:
                sum_val= int(num2[ind_num2]) + +carry
                if sum_val >9:
                    ans.append(str(sum_val)[-1])
                    carry=1
                else: 
                    ans.append(str(sum_val)[0])
                    carry=0
                ind_num2 -=1
        if carry >0:
            ans.append(str(carry))
                
        ans.reverse()
        print(ans)
        return "".join(ans)
                
            
