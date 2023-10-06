# 사용자로부터 3개의 정수를 입력 받고 해당 숫자들을 삼각형을 구성하는 각 변의 길이로 삼을 수 있는지 판단하는 프로그램을 작성하세요. 만약 가능하다면 "Possible", 불가능하다면 "Impossible"을 출력하도록 하세요.
# 삼각형의 조건: 두 변의 길이의 합이 나머지 한 변의 길이보다 반드시 커야 한다.

Values = []
Values.append(input("3개의 정수를 입력해주세요: "))

for values in Values:
    number1 = int(values[0])
    number2 = int(values[1])
    number3 = int(values[2])

    if number1 + number2 > number3 and number2 + number3 > number1 and number3 + number1 > number2:
        print("Possible")
    else:
        print("Impossible")