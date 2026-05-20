import random
class Baseballgame:
    def __init__(self):
        self.correct=[]
        self.life=9
        self.out=0 
        self.hint_count=0

    def make_answer(self):
        self.correct = random.sample(range(1, 10), 4)

    def check(self, user, answer):
        strike=0
        ball=0
        for i in range(4):
            if user[i]==answer[i]:
                strike+= 1
            elif user[i] in answer:
                ball+=1
        return strike, ball

    def get_hint(self):
        hint_num = random.choice(self.correct)
        print(f"힌트: 정답에 {hint_num} 이 포함되어 있습니다!")
        self.hint_count += 1


    def play(self):
        self.make_answer()
        print("[야구게임 시작] 목숨: 9개")

        while self.life > 0:
            print(f"목숨: {self.life} | 아웃: {self.out}")
            user_input = input("4자리 숫자 입력: ")

            if len(user_input) != 4:
                print("4자리를 입력하세요.")
                continue

            user = []
            for i in user_input:
                user.append(int(i))

            if len(set(user)) != 4:
                print("중복 없이 입력하세요.")
                continue

            # 스트라이크 / 볼
            strike, ball = self.check(user, self.correct)
            out = 4 - strike - ball
            self.out += out

            print(f"{strike} 스트라이크 / {ball} 볼 / {out} 아웃")

            # 승리
            if strike == 4:
                print("4스트라이크! 정답입니다!")
                return
            else: 
                self.life -= 1

            # 힌트 조건 
            if self.out >= 3 * (self.hint_count + 1) and self.hint_count < 2:
                print("아웃 3번 누적! 힌트가 생겼습니다.")
                use_hint = input("힌트를 사용하시겠습니까? (예/아니오): ")
                if use_hint == "예":
                    self.get_hint()

        # 패배
        print(" 목숨 소진! <<패>>")
        print("종료합니다.")