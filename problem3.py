# 사용자로부터 자연수를 입력 받아 해당 숫자가 소수인지 판별하는 프로그램을 작성하세요.
# 소수는 1과 자기 자신으로 밖에 나뉘지 않는 자연수입니다. 참고로 1은 소수가 아닙니다.

value = int(input("자연수를 입력하세요: "))

if value == 1:
    print("소수가 아닙니다.")
else:
    for i in range(2, value+1):
        if value % i == 0:
            break
    if value != i:
        print("소수가 아닙니다.")
    else:
        print("소수입니다.")