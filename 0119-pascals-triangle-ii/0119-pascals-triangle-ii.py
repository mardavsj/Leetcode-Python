class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        else:
            pre = []
            pre.append(1)
            for i in range(1, rowIndex+1):
                curr = []
                curr.append(1)
                for j in range(0, len(pre) - 1):
                    curr.append(pre[j]+pre[j+1])
                curr.append(1)
                pre = curr

            return pre
        