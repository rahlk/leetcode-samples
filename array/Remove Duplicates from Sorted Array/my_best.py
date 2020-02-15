class Solution(object):
    def containsDuplicate(self, a):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        a=list(sorted(a))
        f=0
        for i in range(1,len(a)):
            if(a[i]==a[i-1]):
                f=1
                break
            else:
                f=0
        
        if(f==1):
            return True
        else:
            return False
