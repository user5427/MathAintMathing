from random import shuffle

ballList1 = []
white = 18
black = 10

for i in range(0, white):
    ballList1.append(1)
for i in range(0, black):
    ballList1.append(0)
    
# shuffle the list
shuffle(ballList1)

ballList2 = []
white2 = 6
black2 = 17

for i in range(0, white2):
    ballList2.append(1)
for i in range(0, black2):
    ballList2.append(0)
    
# shuffle the list
shuffle(ballList2)


k = 15

repeations = 3000000
# take k balls from the first list randomly and put them in the second list
# then take one ball from second list and check if it is white, calculate the probability of this event
count = 0
for i in range(0, repeations):
    copy1 = ballList1.copy()
    copy2 = ballList2.copy()
    shuffle(copy1)
    
    for j in range(0, k):
        copy2.append(copy1.pop())
        
    shuffle(copy2)
        
    if copy2.pop() == 1:
        count += 1
        
print(count / repeations)