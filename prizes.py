import random
import time

# ──────────────────────────────────────────────
#  🎁 럭키박스 설정  
# ──────────────────────────────────────────────
PRIZES = [
    {"name": "☕ 스타벅스 아이스 아메리카노 (※사정에 따라 변경될 수 있습니다.)", 
     "msg": "축하드립니다.",  "weight": 5},
    {"name": "💆 안마 쿠폰",                                                            
      "msg": "거절도 가능^^", "weight": 20},
    {"name": "🥤 탕비실 고급 커피 무제한 이용권",                                       
     "msg": "커피는 커피!(self)",  "weight": 20},
    {"name": "🪙 현금 500원 (KBC뱅크)",                                            
     "msg": "든든한 후원자",  "weight": 55},
]

# ──────────────────────────────────────────────
#  럭키박스 메인 함수
# ──────────────────────────────────────────────
def random_prize_draw(player_won: bool):
    """
    player_won=True  → 럭키박스 뽑기 진행
    player_won=False → 뽑기 불가 안내 후 종료
    """
    if not player_won:
        print("\n😢 게임에서 지셨습니다. 럭키박스는 승리해야 뽑을 수 있어요!\n")
        return None  # 뽑기 실패 → None 반환

    print("\n" + "🎁 " * 15)
    print("🎉 축하합니다! 숫자 야구 승리 기념 [럭키박스 뽑기]!")
    print("👉 1 ~ 100 사이의 숫자를 하나 고르면 럭키박스가 열립니다!")


    # 1~100 숫자 입력받기
    while True:
        try:
            print("\n📦 1부터 100까지의 숫자 중 하나를 선택하세요.")
            choice = int(input("👉 숫자 입력 (1~100): "))
            if 1 <= choice <= 100:
                break
            print("❌ 1부터 100 사이의 숫자만 입력 가능합니다.")
        except ValueError:
            print("❌ 숫자만 입력 가능합니다.")

    print(f"\n선택하신 번호는 [{choice}]번! 럭키박스를 여는 중입니다... 📦")
    print("두구두구두구... 과연 어떤 사은품이?! 🥁")
    time.sleep(2)

    # 확률에 따라 상품 뽑기
    weights = [p["weight"] for p in PRIZES]
    final_prize = random.choices(PRIZES, weights=weights, k=1)[0]

    print("\n" + "=" * 60)
    print(f"✨ 결과 발표: {choice}번 럭키박스에서 나온 사은품은?")
    print(f"👉 [{final_prize['name']}]")
    print(f"   {final_prize['msg']}")
    print("=" * 60)
    print("🎬 축하합니다! 게w임이 최종 종료되었습니다.\n")

    return final_prize  # 당첨 상품 dict 반환 (팀원 코드와 연결할 때 사용)


# ──────────────────────────────────────────────
#  단독 실행 테스트 (통합할 때는 아래 블록 생략)
# ──────────────────────────────────────────────
if __name__ == "__main__":
    result = input("게임 결과 입력 (win / lose): ").strip().lower()
    random_prize_draw(player_won=(result == "win"))