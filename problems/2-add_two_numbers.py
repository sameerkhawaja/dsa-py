class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        gp = dummy

        while True:
            kth = self.getKth(gp, k)
            if not kth:
                break
            gn = kth.next

            # reverse group
            p, c = kth.next, gp.next
            while c != gn:
                n = c.next
                c.next = p
                p = c
                c = n

            x = gp.next
            gp.next = kth
            gp = x
        return dummy.next

    def getKth(self, c, k):
        while c and k > 0:
            c = c.next
            k -= 1
        return c

    # if(numdict.get(dict) == None):
    #     numdict[dict] = 0
    # elif numdict[dict] == 0:
    #     numdict[dict] = 1
    # else:
    #     numdict[dict] = numdict[dict] * (numdict[dict] + 1) // 2
    #     print(numdict[dict])
