class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Helper function to perform depth-first search for permutation generation
        def backtrack(index):
            # If the current index has reached the length of nums list,
            # we have a complete permutation
            if index == len_nums:
                permutations.append(current_permutation[:])
                return
          
            # Iterate over the nums list to create permutations
            for j in range(len_nums):
                # Check if the number at index j is already used in the current permutation
                if not visited[j]:
                    # If not visited, mark it as visited and add to current permutation
                    visited[j] = True
                    current_permutation[index] = nums[j]
                    # Recurse with next index
                    backtrack(index + 1)
                    # Backtrack: unmark the number at index j as visited for the next iteration
                    visited[j] = False

        len_nums = len(nums)  # Store the length of the input list
        visited = [False] * len_nums  # Create a visited list to track numbers that are used
        current_permutation = [0] * len_nums  # Temp list to store the current permutation
        permutations = []  # Result list to store all the permutations
        backtrack(0)  # Start generating permutations from index 0
        return permutations


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.perms = []
        
        self.dfs([])
        return self.perms
    
    def dfs(self, crnt_set: List[int]):
        if len(crnt_set) == len(self.nums):
            self.perms.append(crnt_set.copy())
            return
        
        for num in self.nums:
            if num in crnt_set:
                continue
            
            crnt_set.append(num)
            self.dfs(crnt_set)
            crnt_set.pop()