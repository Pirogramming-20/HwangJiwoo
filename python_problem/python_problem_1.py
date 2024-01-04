from random import randint

num = 0
# 차례
player = "computer"

def br_Game(player, num):
  if player == "computer":
    computer_input = randint(1, 3)
    cnt = computer_input
    for i in range(cnt):
      num += 1
      print(player + " :", num)
      if num == 31:
        return num
    return num
  else:
    while True:
      user_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
      try:
        user_input = int(user_input)
        if user_input in (1, 2, 3):
          cnt = user_input
          for i in range(cnt):
            num = num + 1
            print(player + " :", num)
            if num == 31:
              return num
          return num
        else:
          print("1,2,3 중 하나를 입력하세요")
      except ValueError:
        print("정수를 입력하세요")

while num < 31:
  num = br_Game(player, num)
  if (player == "computer"):
    player = "player"
  else:
    player = "computer"

print(player + " win!")