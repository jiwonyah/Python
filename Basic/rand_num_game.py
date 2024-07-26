# Recap & Newly get)
# a, b = map(int, input("a and b?: ").split())
#
# shift + tab 누르면 indentation 내어쓰기 가능한 거 처음 알았다.
#
# upper(), capitalize(), replace("o", "i")
# startswith("n") --> bool
#
#-----------------------------------------------------------------------------------------
"""
노마드 코더 강의 cazino 문제: https://nomadcoders.co/python-for-beginners/lectures/3776

*** 내 맘대로 버전 *** 
 설명)
   - 컴퓨터가 생성하는 난수 맞추기 게임
 추가 요소)
   - 정답을 맞출 때까지 반복
   - 정답 맞추고 나면 새로운 게임 제안
"""

# Module: Random
# from module import function
# from random import randint

# def new_game_prompt():
#     while True:
#         after_correct = input("Do you want a new game? (y/n) ").upper()
#         if after_correct == 'Y':
#             print("""======================================\n
#                     New game is now being loaded...""")
#             play_game()
#             break
#         elif after_correct == 'N':
#             print("See you later!")
#             break
#         else:
#             print("select (y/n)")
            
# def play_game():
#     answer = randint(1, 50)
#     print("System) Answer: ", answer)
#     user_choice=0 #initialize
#     try:
#         while user_choice != answer:  #유저가 고른 답과 answer가 다르면 반복
#             user_choice = int(input("Choose your number(1~50): "))
#             if user_choice == answer:
#                 print("You win!")
#                 new_game_prompt()
#             elif user_choice < answer:
#                 print("Higher!")
#             else:
#                 print("Lower!")
#     except ValueError as e:
#         print(e)
        
# play_game()


#-------------------------------------------------------------------------------------------------
# 노마드 풀이
from random import randint

print("Welcome to Cazino")
pc_choice = randint(1,50)
playing = True

while playing:
    user_choice = int(input("Choose Number (1- 50): "))
    if user_choice == pc_choice:
        print("You win!")
        playing = False
    elif user_choice < pc_choice:
        print("Higher")
    elif user_choice > pc_choice:
        print("Lower!")
    



