import math

t = int(input())

for i in range(t):
    score = []
    teams = int(input())
    for j in range(teams):
        a = [j+1]
        b = list(map(int, input().split()))
        a.append(b)
        score.append(a)
    #print(score)
    rounds = math.log(teams,2)
    #print(rounds)
    rounds = int(rounds)
    for l in range(rounds):
        score.sort()
        #print(score)
        for k in range(len(score)//2):
            t1 = 0
            t2 = 0
            #print(score[k])
            #print(score[k+1])
            for t in range(5):
                if score[k][1][t]>score[k+1][1][t]:
                    t1 = t1 + 1
                else:
                    t2 = t2 + 1
            if (t1>t2):
                score.pop(k+1)
            else:
                score.pop(k)
    print(score[0][0])

