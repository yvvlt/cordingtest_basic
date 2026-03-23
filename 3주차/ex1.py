menu = {"커피":2000, "라떼":2500, "그린티":3000,"카페모카":3500, "카푸치노":4000}

price = 0
buy_list = []


while(True):
    print("\n", menu, "\n")
    choice = input("원하시는 메뉴를 고르세요: ('0' 입력 시 종료): ")

    if choice == "0":
        print("안녕히 가세요")
        break

    elif choice in list(menu.keys()):
        print(menu[choice])
        buy_list.append(choice)
        price = price + menu[choice]

    elif choice == "계산":
        print("주문하신 메뉴: ", buy_list)
        print("가격은 ", price, "입니다.")
        print("감사합니다.")
        break

    else:
        print("다시 입력해주세요. == \n")