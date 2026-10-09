class Solution:
    def isPalindrome(self, arr):
        # code here
        n=len(arr)
        left=0
        right=n-1
        for i in range(n):
            while left<right:
                if arr[left]==arr[right]:
                  left=left+1
                  right=right-1
                else:
                    return False
            return True
