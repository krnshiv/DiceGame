from users import User
from Ranking import RankTree
from dice import Dice
import random

def MainGameService(n,m):
  
    Players = add_players(n)
    ordering=[i for i in range(1,n+1)]
    pick_order(ordering)
    n+=1
    ranks=[]
    current_player=0

    while(ordering):
        print(n)
        x = play_round(Players,ordering,n,m,current_player-1)
        ranks.append({'id':ordering.pop(x),'rank':len(ranks)+1})
        current_player=(x)%(n-1)    # rogin-round
        n=n-1
        print(ordering)
        print("**FINAL RANKING TABLE**")
        print('--------------------------')
        print("  Player  Rank ")
        print('--------------------------')
        for i,val in enumerate(ranks):
            print('| Player',val['id']," ",'',val['rank'],'  |')
    
#function to execute play till one member hit 'm' points
def play_round(Players,ordering,n,m,current_player):
    print(m,current_player)
    current_player = current_player
    while True:
        
        ranker = RankTree(-1,-1)
        r = input('Player'+str(ordering[current_player])+"turn to roll,Press r to roll the dice")
        if r:
            #check whether a player has been penalized
            if not Players[ordering[current_player]].is_penalized:
                d=Dice.roll()
                print('Dice Roll: ',d)
                Players[ordering[current_player]].score+=d
                print('score of Player',ordering[current_player]," ",Players[ordering[current_player]].score)
                if Players[ordering[current_player]].score >= m:
                    return current_player

            #if and while the dice keeps rolling out a six
                while d==6:
                    d = Dice.roll()
                    print('Dice Roll: ',d)
                    Players[ordering[current_player]].score+=d
                    
                    if Players[ordering[current_player]].score >= m:
                        return current_player

            #if 1 did roll up more than once consecutively
                if d==1 and Players[ordering[current_player]].last_roll==1:
                    Players[ordering[current_player]].is_penalized=True
                
            #Score check
                if Players[ordering[current_player]].score >= m:
                    return current_player

            #function to get unction to get curent ranking of all players still in the Game after rolled Dice using inorder traversal

                for i in ordering:
                    ranker.add(i,Players[i].score)
                get_ranking(ranker)

            #updated last_rolled value
                Players[ordering[current_player]].last_roll=d

            #after one Move skip we can unpenialize
            else:
                Players[ordering[current_player]].is_penalized=True
            
            current_player+=1
            current_player=current_player%(n-1) #robin-round


#function to get ranking after every move using inorder traversal
def get_ranking(ranker):
    curr = ranker
    arr=[]
    stack=[]
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        m = stack.pop()
        arr.append([m.id,m.val])
        curr = m.right
    print("**CURRENT RANKING TABLE**")
    print('--------------------------')
    print("   Player    Rank  Score")
    print('--------------------------')
    for i,val in enumerate(reversed(arr[1::])):
        print('|  Player',val[0]," ",i+1,'',val[1],'  |')

#function to randomize order
def pick_order(order):
     random.shuffle(order)

#function to add player and create User objects
def add_players(n):
    players={}
    x=100
    for i in range(1,n+1):
        u = User(i)
        players[u.id]=u    
    return players


if __name__=="__main__":
    n= input('Enter the Number of Players')
    m = input('Enter Points to be accumalated')
    MainGameService(int(n),int(m))