readList = input().split("|")
emp_m = []
k = -2
Alice_total = 0
Bob_turn = 0
Alice_turn = 0
Bob_total = 0
brains = [Alice_total, "", Bob_turn, Alice_turn, Bob_total]
emptyStr = False
shotGuns = [Alice_total, "", Bob_turn, Alice_turn, Bob_total]
i = 0
z = 0
y = 0
x = []
m = 1
temp = 0

if readList[0] == "":
    emptyStr = True
#Alice's turn

# generate all possible m values and store them into a list to see which one is optimal
# m can be changed as the reader wishes
while m < 10 :
    i = 0
    while i < len(readList):

        if brains[k] <= m and k == -2 and not emptyStr:

            for j in range(3) :

              if i == len(readList):
                break
              else:
                # tally score of indivial turn
                if readList[i][j] == "B":
                    brains[k] += 1
                if readList[i][j] == "S":
                    shotGuns[k] += 1
                if shotGuns[k] >= 3:
                    brains[k] = 0

            if i != len(readList):
                i += 1
            # if any 1 of 3 conditions is satisfied, tally one's score and alternate to another player
            if shotGuns[k] >= 3 or brains[k] >= m or i == len(readList):
                brains[k+2] += brains[k]
                brains[k] = 0
                shotGuns[k] = 0
                k = (-1) * k
#Bob's turn
        if brains[k] <=3 and k == 2 and not emptyStr:
          # identical codes as above except Bob sticks with rule of 3 here.

            for j in range(3) :

                if i == len(readList):
                    break
                else:
                    if readList[i][j] == "B":
                        brains[k] += 1
                    if readList[i][j] == "S":
                        shotGuns[k] += 1
                    if shotGuns[k] >= 3:
                        brains[k] = 0

            if i != len(readList):
                i += 1

            if shotGuns[k] >= 3 or brains[k] >= 3 or i == len(readList):
              # k = 2 is Bob's each turn score, k = 2 + 2 is Bob's total score
                brains[k+2] += brains[k]
                brains[k] = 0
                shotGuns[k] = 0
                k = (-1) * k

    temp = (brains[0], brains[4], m)
    emp_m.append(temp)


    brains[0] = 0
    brains [4] = 0
    m +=1

# sort those values in ascending order based on the number of total brains
x = sorted(emp_m)
i = 0
y = 0

# returns the M value associated with the biggest total brains
# if multiple Ms give the same biggest total brains, return the smallest M.
while z < len(x) - 1:
    if x[-1 - z][0] == x[-2 - z][0]:
       y = x[-2 - z][2]
    else:
       y = x[-1 - z][2]
       break
    z += 1

print("Alice's optimal strategy is to stick with rule of ", y)

print("scores: Alice", sorted(emp_m)[-1][0], ", Bob", sorted(emp_m)[-1][1])

# Sample input and output: 
#        input: BSS|BFS|BBF|SFS|SBF|BSB|SSF|BSB|BBB|FFB|BSS 
#        output:  Alice's optimal strategy is to stick with rule of 2; 
#                 scores:  Alice 5 , Bob 2"
#
# Note that this program returns Alice's optimal strategy in terms of finding the m that gives Alice the most brains
# However this is not necessarily always the best strategy to win the game.
# Consider the following case: input: BSS|BFS|BBF|SFS|SBF. 
#                              output: Alice's optimal strategy is to stick with rule of  1
#                                      scores: Alice 1 , Bob 3
# Alice scores the most brains possible, which is 1 in this case, when m = 1; however, if Alice chooses m to be 2
# then both Alice and Bob score 0 brain, in which case Alice's relative position is better comparing to " Alice 1 , Bob 3"
