from .BaseballGame import Baseballgame
from .luckbox import random_prize_draw
from .b31_game import Baskin31Game

class App:
    def print_menu():
        print("\n====== GAME MENU ======")
        print("1. 야구게임")
        print("2. 베스킨라빈스31")
        print("3. 럭키박스")
        print("4. 종료")


    while True:
        print_menu()

        menu = input("메뉴를 선택하세요: ")

        # 야구게임
        if menu == "1":
            game = Baseballgame()
            game.play()

        # 베스킨라빈스31
        elif menu == "2":
            game31 = Baskin31Game()
            game31.start_game()

        # 럭키박스
        elif menu == "3":
            random_prize_draw()

        # 종료
        elif menu == "4":
            print("게임을 종료합니다.")
            break

        else:
            print("올바른 메뉴를 입력하세요.")