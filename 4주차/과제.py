while True:
    # 시작값 입력 (0 입력 시 프로그램 종료)
    n = int(input("몇 팩토리알?(0 입력시 종료): "))
    if n == 0:
        print("안녕 잘가")
        break
    # 시작값이 1보다 작으면 다시 입력받기
    if n < 1:
        print("팩토리알은 1 이상이어야 해! 다시 입력해!")
        continue

    # 종료값 입력 (0 입력 시 종료)
    m = int(input("어디서 멈출래?: "))
    if m == 0:
        print("안녕 잘가")
        break
    # 종료값이 1보다 작으면 다시 처음부터 시작
    if m < 1:
        print("아니 너무 작잖어! 다시 입력해!")
        continue
    # 종료값이 시작값보다 크면 다시 처음부터 시작
    if m > n:
        print("아니 너무 크잖어! 다시 입력해!")
        continue

    factors = []  # 곱할 숫자들을 저장할 리스트
    result = 1    # 결과값 저장할 변수 (곱셈 결과)

    # n부터 m까지 내림차순으로 반복하여 곱셈하고 factors에 문자열로 저장
    for i in range(n, m - 1, -1):
        factors.append(str(i))  # 곱할 수를 문자열 형태로 리스트에 추가
        result *= i             # 곱셈 결과 업데이트

    # 곱셈 과정 문자열 생성 
    formula_str = " * ".join(factors)
    # 결과 출력
    print(f"{n} ! :{formula_str} = {result}")