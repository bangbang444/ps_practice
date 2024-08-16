num = int(input())

numerator = 1 # 분자
denomiator = 1 # 분모
count = 0

while True:
    if count == num and num == 1:
        print("1/1")
        break
    elif count == num:
        break

    if numerator == 1:
        denomiator += 1         
    elif denomiator == 1:
        numerator+=1

    while True:
            numerator+=1
            denomiator-=1

            if denomiator == 1 or numerator == 1:
                break

print(f"{numerator}/{denomiator}")