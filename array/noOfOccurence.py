n = 6
x = 12
arr = [8,9,10,12,12,12]
# Output: 4

#User function Template for python3
class Solution:

	def count(self,arr, n, x):
	    count = 0
	    for i in range(n):
	        if arr[i] == x:
	            print(arr[i])
	            count +=1
	        else:
	           continue
	       
	   # print(count)
	    return count

	            
		# code here
		
obj = Solution()
c=obj.count(arr, n, x)
print("c",c)
