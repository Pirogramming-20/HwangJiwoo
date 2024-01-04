num = 0
# 부를 숫자의 수
cnt = 0

while True:
  user_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
  try:
      user_input = int(user_input)
      if user_input in (1, 2, 3):
          cnt = user_input
          break
      else:
          print("1,2,3 중 하나를 입력하세요")
  except ValueError:
      print("정수를 입력하세요")

for i in range(cnt):
  num = num + 1
  print("playerA :", num)

while True:
  user_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
  try:
      user_input = int(user_input)
      if user_input in (1, 2, 3):
          cnt = user_input
          break
      else:
          print("1,2,3 중 하나를 입력하세요")
  except ValueError:
      print("정수를 입력하세요")

for i in range(cnt):
  num = num + 1
  print("playerB :", num)