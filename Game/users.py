class User:
    def __init__(self,id,score=0,last_roll=None):
        self.id = id
        self.score = score
        self.last_roll = last_roll
        self.is_penalized = False
        self.rank = None

    def __repr__(self):
        return str(self.id)+'_'+str(self.score)+'_'+str(self.rank)
    def penalize(self):
        self.is_penalized=True

    def update_rank(self,rank):
        self.rank = rank
    
    def update_score(self,score):
        self.score = score
    
    def update_last_roll(self,last_roll):
        self.last_roll = last_roll
    
