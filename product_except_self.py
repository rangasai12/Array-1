class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_array = [None]*len(nums)
        left_array[0]=1
        for i in range(1,len(nums)):
            left_array[i]=left_array[i-1]*nums[i-1]

        right_array = [None]*len(nums)

        right_array[-1]=1

        for i in range(len(nums) - 2, -1, -1):
            right_array[i] = right_array[i+1]*nums[i+1]
        
        result_array = [None]*len(nums)
        for i in range(len(left_array)):
            result_array[i] = left_array[i]*right_array[i]

        
        

        print(result_array)

        return result_array
