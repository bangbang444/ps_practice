tcase = int(input())

winner_list = []

over_num = -1
for i in range(tcase):
    person_num = int(input())
    max = -1
    sum = 0
    if person_num == 0:
        winner_list.append([-1, -1])
        continue

    for j in range(person_num):
        vote = int(input())
        sum += vote
        if max < vote:
            max = vote
            win_number = j+1
            continue
        
        if max == vote:
            over_num = vote
    

    if max == over_num:
        winner_list.append([-1, -1])
    elif sum/2 < max:
        winner_list.append([win_number, 1])
    elif sum/2 >= max:
        winner_list.append([win_number, 2])
        


for winner in winner_list:
    if winner[1] == -1:
        print("no winner")
    elif winner[1] == 1:
        print(f"majority winner {winner[0]}")
    elif winner[1] == 2:
        print(f"minority winner {winner[0]}")
