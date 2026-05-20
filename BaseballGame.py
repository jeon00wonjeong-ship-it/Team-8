import random
class BaseballGame:
    def __init__(self):
        self.correct=[]
        self.life=9
        self.out=0 
        self.hint=0

    def make_answer(self):
        self.correct = random.sample(range(1, 10), 4)

    def check(self, user, answer):
        strike=0
        ball=0
        for i in range(1,4):
            if user[i]==answer[i]:
                strike+= 1
            elif user[i] in answer:
                ball+=1
        return strike, ball

    def get_hint(self):

    def play(self):
        self.answer=self.make_answer()
        #123
        5