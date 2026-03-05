import random

def start_game():
    print("--- 歡迎來到猜數字冒險！ ---")
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("請輸入一個 1 到 100 之間的數字："))
            attempts += 1
            
            if guess < target_number:
                print("太小了！再試一次。")
            elif guess > target_number:
                print("太大了！再試一次。")
            else:
                print(f"恭喜你！你花了 {attempts} 次猜中了數字 {target_number}！")
                break
        except ValueError:
            print("請輸入有效的整數。")

if __name__ == "__main__":
    start_game()
