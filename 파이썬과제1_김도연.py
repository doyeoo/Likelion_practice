likelion={'현숙':"이화여대 멋사 대표님", '두희':"멋사 창립자", '세은':"파이썬 세션 튜터", '마루':"야옹"}

for key, value in likelion.items():
    print("다음은 누구에 대한 설명일까요?")
    print(value)
    print("1.현숙 2.세은 3.두희 4.마루")
    
    input_key=input()

    if input_key==key:
        print("정답입니다!")
    else:
        print("오답입니다!")
    print("\n")
