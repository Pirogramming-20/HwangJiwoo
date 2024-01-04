num = 0
# 부를 숫자의 수
cnt = 0
# 게임을 계속할 지를 결정
flag = True

while flag:
  while flag:
    user_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
    try:
      user_input = int(user_input)
      if user_input in (1, 2, 3):
        cnt = user_input
        for i in range(cnt):
          num = num + 1
          print("playerA :", num)
          if num == 31:
            flag = False
            print("playerB win!")
            break
        break
      else:
        print("1,2,3 중 하나를 입력하세요")
    except ValueError:
      print("정수를 입력하세요")

  while flag:
    user_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
    try:
      user_input = int(user_input)
      if user_input in (1, 2, 3):
        cnt = user_input
        for i in range(cnt):
          num = num + 1
          print("playerB :", num)
          if num == 31:
            flag = False
            print("playerA win!")
            break
        break
      else:
        print("1,2,3 중 하나를 입력하세요")
    except ValueError:
      print("정수를 입력하세요")