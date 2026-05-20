import random

class Baskin31Game:
    def __init__(self):
        # 게임의 시작 상태 초기화
        self.current_number = 0  # 누적되는 현재 숫자를 저장하는 변수

    def get_user_input(self):
        # 1) 사용자에게 입력값 받기
        while True:
            print(f"\n[현재 숫자: {self.current_number}]")
            user_input = input("연속된 숫자를 입력하세요 (예: 1 2 3 또는 1,2): ")
            
            # 쉼표(,)가 있으면 공백으로 바꾸고, 공백을 기준으로 글자들을 쪼개서 리스트로 만듦
            clean_input = user_input.replace(",", " ")
            input_list = clean_input.split()
            
            # 1. 아무것도 입력하지 않은 경우_예외 처리
            if not input_list:
                print("오류: 숫자를 최소 하나 이상 입력해야 합니다.")
                continue
                
            try:
                # 입력받은 문자열 리스트로 변환
                numbers = [int(num) for num in input_list]
                
                # 2. 개수 검증 (1개에서 3개까지만 입력)
                if len(numbers) < 1 or len(numbers) > 3:
                    print("오류: 한 번에 1개에서 3개의 숫자만 입력할 수 있습니다.")
                    continue
                
                # 3. 연속성 및 올바른 숫자 검증
                is_valid = True
                expected = self.current_number + 1
                for num in numbers:
                    if num != expected:
                        is_valid = False
                        break
                    expected += 1
                
                if is_valid:
                    return numbers  # 검증을 모두 통과하면 숫자 리스트 반환
                else:
                    print(f"오류: {self.current_number + 1}부터 시작하는 올바른 연속된 숫자를 입력해야 합니다.")
                    
            except ValueError:
                print("오류: 숫자만 입력할 수 있습니다.")

    def play_turn(self, player_name, numbers):
        # 2) 지정된 갯수만큼 숫자를 연속으로 부를때
        print(f"{player_name}: ", end="")
        
        for num in numbers:
            self.current_number = num
            print(self.current_number, end=" ")
            if self.current_number >= 31:
                break
        print()

    def start_game(self):
        # 전체 게임의 진행 순서
        print("\n[ 베스킨라빈스 31 게임 룰! ] ===============================")
        print("1) 숫자 1부터 시작해 차례대로 숫자를 부릅니다.")
        print("2) 자신의 차례에 숫자는 최대 3개까지 가능합니다.")
        print("3) 여러개의 숫자 입력의 경우, 꼭 '띄어쓰기'와 ',(쉼표)'를 포함해 입력해주세요")
        print("4) 마지막에 31을 부르는 사람이 패배합니다.")
        print("======================================================")

        # 숫자가 31 미만인 동안 사용자와 컴퓨터가 번갈아가며 진행
        while self.current_number < 31:
            # 1. 사용자 차례 (함수 이름을 get_user_input으로 올바르게 매칭)
            user_numbers = self.get_user_input()
            self.play_turn("당신", user_numbers)
            
            if self.current_number >= 31:
                print("\n당신이 31의 숫자를 불러서, 게임에서 '패배'했습니다!!")
                break

            # 2. 컴퓨터 차례
            com_numbers = []
            next_num = self.current_number + 1
            
            # 컴퓨터가 몇 개의 숫자를 부를지 1~3 사이로 무작위 결정
            com_count = random.randint(1, 3) 
            
            # 결정된 개수(com_count)만큼 반복문을 수행하도록 수정
            for _ in range(com_count):
                if next_num > 31:
                    break
                com_numbers.append(next_num)
                next_num += 1
                
            self.play_turn("상대", com_numbers)
            
            if self.current_number >= 31:
                print("\n축하합니다!! 상대가 31을 불러서, 당신이 '승리'했습니다!!!!")
                break

""" # 실제 게임 실행 부분(확인용)
if __name__ == "__main__":
    game = Baskin31Game()
    game.start_game() """