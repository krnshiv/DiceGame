
class RankTree:
    def __init__(self,i, val):
        self.id = i
        self.val = val
        self.leftsize = 0
        self.left = self.right = None
    
    def add(self,i,val):
        
        if val <= self.val:
            self.leftsize+=1
            if self.left:
                return self.left.add(i,val)
            else:
                self.left = RankTree(i,val)
                return 0
        elif val>self.val:
            if self.right:
                return self.leftsize +1+self.right.add(i,val)
            else:
                self.right = RankTree(i,val)
                self.right.val = val              
                return self.leftsize + 1
       