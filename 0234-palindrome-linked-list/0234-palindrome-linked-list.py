class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pointer = head
        arr = []
        while pointer:
            arr.append(pointer.val)
            pointer = pointer.next
        
        n = len(arr)
        for i in range(n//2):
            if arr[i] != arr[n-1-i]:
                return False
        return True