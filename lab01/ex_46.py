import random
import pprint

N = int(input("몇 게임? "))


def lottery_game():
    lottery = []

    while len(lottery)<6:
        n = random.randrange(1,46)

        if n not in lottery:
            lottery.append(n)
        
        #방법 2
        # if not (n in lottery):
        #     lottery.append(n)
            
    #방법3
        # dup = False
        # for j in lottery:
        #     if n == j:
        #         dup = True
        
        # if dup == False:
        #     lottery.append(n) 
    return lottery
pprint.pprint(
    [lottery_game()for _ in range(N)],
    width=50
)

