class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        p_nums = []
        n_nums = []
        z_nums = []
        nums.sort()
        for n in nums:
            if n > 0:
                p_nums.append(n)
            elif n < 0:
                n_nums.append(n)
            else:
                z_nums.append(n)
                
        # [0, 0, 0]:
        if len(z_nums) > 2:
            results.append([0, 0, 0])
        
        # [1 negative, 0 , 1 positive]:
        if len(n_nums) > 0 and len(p_nums) > 0:
            if z_nums:
                p0 = 0
                p1 = len(nums) - 1
                while p0 < p1 and nums[p0] != 0 and nums[p1] != 0:
                    if nums[p0] + nums[p1] == 0:
                        if not results:
                            results.append([nums[p0], 0, nums[p1]])
                        elif results[-1] != [nums[p0], 0, nums[p1]]:
                            results.append([nums[p0], 0, nums[p1]])
                        p0 += 1
                        p1 -= 1
                    elif nums[p0] + nums[p1] < 0:
                        p0 += 1
                    else:
                        p1 -= 1
            
        
        # [1 negative, 2 positive]:
        if len(n_nums) > 0 and len(p_nums) > 1:
            for n in set(n_nums):
                p0 = 0
                p1 = len(p_nums) - 1
                while p0 < p1:
                    if p_nums[p0] + p_nums[p1] + n == 0:
                        if not results:
                            results.append([n, p_nums[p0], p_nums[p1]])
                        elif results[-1] != [n, p_nums[p0], p_nums[p1]]:
                            results.append([n, p_nums[p0], p_nums[p1]])
                        p0 += 1
                        p1 -= 1
                    elif p_nums[p0] + p_nums[p1] + n < 0:
                        p0 += 1
                    else:
                        p1 -= 1
        
        # [2 negative, 1 positive]:
        if len(n_nums) > 1 and len(p_nums) > 0:
            for n in set(p_nums):
                p0 = 0
                p1 = len(n_nums) - 1
                while p0 < p1:
                    if n_nums[p0] + n_nums[p1] + n == 0:
                        if not results:
                            results.append([n_nums[p0], n_nums[p1], n])
                        elif results[-1] != [n_nums[p0], n_nums[p1], n]:
                            results.append([n_nums[p0], n_nums[p1], n])
                        p0 += 1
                        p1 -= 1
                    elif n_nums[p0] + n_nums[p1] + n < 0:
                        p0 += 1
                    else:
                        p1 -= 1

        return results
            
                
            
        
            
                
        
        