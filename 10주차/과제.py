def check_palindrome(text):
    #스택 역할리스트 만들기
    stack = []
    length = len(text)
    
    #앞 절반 글자를 스택에 넣기
    for i in range(length // 2):
        stack.append(text[i])
    
    #글자 수가 홀수면 가운데 글자 건너뛰기
    if length % 2 == 1:
        start = (length // 2) + 1
    else:
        start = length // 2
    
    #뒤 글자와 스택에서 꺼낸 글자 하나씩 비교하기
    for i in range(start, length):
        if len(stack) == 0:  # 스택이 비었으면 False
            return False
        if stack.pop() != text[i]:  # 다르면 회문 아님
            return False
    
    # 모두 같으면 True, 아니면 False
    return len(stack) == 0


def main():
    while True:
        word = input("문장을 입력해주세요(x 입력시 종료): ")
        if word == 'x' or word == 'X':  # x 입력하면 끝내기
            break

        print("입력한 문장:", word)
        print("회문을 검사합니다.")
        
        if check_palindrome(word):
            print(f"문장:'{word}'은/는 회문입니다.\n")
        else:
            print(f"문장:'{word}'은/는 회문이 아닙니다.\n")


if __name__ == "__main__":
    main()