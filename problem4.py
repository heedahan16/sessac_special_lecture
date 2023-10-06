# 사용자로부터 자연수 n을 입력 받아 n 이하의 홀수들의 계승을 구하는 프로그램을 작성하세요.
# 계승(팩토리얼): 1부터 자기 자신까지의 곱의 합

n = int(input("자연수를 입력하세요: "))

print(str(n).ljust(12), end="")
print("!")
print()

for i in range(1, n+1, 2): 
    start = 1
    
    for j in range(1, i+1):
        start *= j

    print(str(i).ljust(12), end="")
    print(start)
