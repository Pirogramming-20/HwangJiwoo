num = 0
cnt = 0

while true:
    value = int(intput("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))

    if type(cnt) != int:
        print("정수를 입력하세요")
    elif cnt < 1 or cnt > 3:
        print("1,2,3 중 하나를 입력하세요")
    else:
        cnt = value
        break