# 사용자로부터 XY 좌표 공간에서의 점의 위치를 입력 받아 해당 점이 몇 사분면에 있는지 판단하는 시스템을 만드세요.

x = int(input("x값을 입력하세요: "))
y = int(input("y값을 입력하세요: "))

if x > 0 and y > 0:
    print("1사분면")
elif x < 0 and y >0:
    print("2사분면")
elif x > 0 and y < 0:
    print("3사분면")
elif x < 0 and y < 0:
    print("4사분면")
elif x == 0 and y == 0:
    print("원점")