total_sum = 0.0
score_sum = 0.0
subject_num = 20
num = 0

G = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

for i in range(subject_num):
    study_info = input()
    _, credit, grade = study_info.split(' ')

    if grade == 'P':
        continue
        
    score_sum += float(credit)
    total_sum += float(credit) * G[grade]

if(total_sum == 0):
    print(0.0)
    exit(0)
print(total_sum/score_sum)


