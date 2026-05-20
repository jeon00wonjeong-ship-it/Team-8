import random

class Hint31Game:
    def __init__(self):
        #게임의 시작 상태 초기화
        self.current_number = 0  # 누적되는 현재 숫자를 저장하는 변수

    def get_user_input(self):
        
        #1)사용자에게 입력값(1~3 개수 받기)
        while True:
            try:
                count = int(input(">> 숫자를 입력해주세요 (3개까지 입력가능): "))
                
                if count in [1,2,3]:
                    return count
                print("오류: 1, 2, 3 중에서만 입력해야 합니다.")
            except ValueError:
                print("오류: 연결된 숫자로만 입력할 수 있습니다.")

    def play_turn(self, player_name, count):
        
        #2)지정된 갯수만큼 숫자를 연속으로 부를때
        print(f"{player_name}: ", end="")
        for _ in range(count):
            self.current_number += 1
            print(self.current_number, end=" ")
            if self.current_number >= 31:
                break
        print()

    def start_game(self):
        
        #전체 게임의 진행 순서
        print("\n힌트를 얻기위한 게임!! ")
        print("\n[ 베스킨라빈스 31 ] ===============================")
        print("1) 숫자 1부터 시작해 차례대로 숫자를 부릅니다.")
        print("2) 자신의 차례에 숫자는 최대 3개까지 가능합니다.")
        print("3) 마지막에 31을 부르는 사람이 패배합니다.")
        print("======================================================")

        # 숫자가 31 미만인 동안 사용자와 컴퓨터가 번갈아가며 진행
        while self.current_number < 31:
            
            # 1. 사용자 턴
            user_count = self.get_user_input()
            self.play_turn("사용자", user_count)
            
            if self.current_number >= 31:
                print("\n사용자턴에서 31의 숫자가 불려서 힌트 얻기 실패!!")
                break

            # 2. 컴퓨터 턴:
            print(f"\n[현재 숫자: {self.current_number}]")
            com_count = random.randint(1, 3)
            self.play_turn("상대", com_count)
            
            if self.current_number >= 31:
                print("\n축하합니다!! 힌트 게임에서의 승리로 '힌트 얻기 성공'!!")
                break


# --- 실제 게임 실행 부분 ---
if __name__ == "__main__":
    game = Hint31Game()
    game.start_game()