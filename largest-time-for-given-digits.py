#https://leetcode.com/problems/largest-time-for-given-digits/description/
#949. Largest Time for Given Digits

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def valid_minutes(min):
            if min <=59:
                return True
            return False

        def min_calculation(reverse_pos):
            pos_list =[x for x in range(4)]
            for val in reverse_pos:
                pos_list.remove(val)
            minute_val1=arr[pos_list[0]] *10 +arr[pos_list[1]]
            minute_val2=arr[pos_list[1]] *10 +arr[pos_list[0]]
            if valid_minutes(minute_val1) and valid_minutes(minute_val2):
                return max(minute_val1,minute_val2)
            elif  valid_minutes(minute_val1) :
                return minute_val1
            elif  valid_minutes(minute_val2) :
                return minute_val2
            return -1
        def backtracking(curr):
            if len(curr) ==2:
                hours =curr[0]*10 +curr[1]
                if hours<=23:
                    minutes =min_calculation(seen)
                    if minutes>-1:    
                     result.append(hours*100+minutes)
                return 
            for val in range(len(arr)):
                if val not in seen:
                    curr.append(arr[val])
                    seen.append(val)
                    backtracking(curr)
                    curr.pop()
                    seen.pop()
            return 
        result =[]
        seen=[]
        backtracking([])
        if len(result) ==0:
            return ""
        latest_time =str(max(result))
        if len(latest_time) <4:
            for i in range((4-len(latest_time))):
                latest_time ='0' +latest_time

        return latest_time[0:(len(latest_time) -2)]+":"+latest_time[(len(latest_time) -2):]
