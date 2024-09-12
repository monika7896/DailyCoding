#  move all zeros at thr end of nums using in-place
# firstly  move non zero elemetn in the starting
class Solution:
    def move_zero_end(self , nums):
        last_non_zero_index = 0

# firstly  move non zero elemetn in the starting

        for i in range(len(nums)):
            if nums[i] !=0 :
                print(nums[i] ,"indexed" ,i)
                print(last_non_zero_index

                nums[last_non_zero_index]= nums[i]
                last_non_zero_index += 1

# here loop will strt like 3 to 5 and then set nums[i] to 0 so all remaining space will be 0
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0          
        return nums
            
  
nums=[0,1,0,3,12]
obj = Solution()
resp = obj.move_zero_end(nums)
print(resp)
