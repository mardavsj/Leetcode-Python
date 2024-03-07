class Solution(object):
    def deleteDuplicates(self, head):
        cursor = head
        while cursor:
            while cursor.next and cursor.val == cursor.next.val:
                cursor.next = cursor.next.next
            cursor = cursor.next
        return head
        