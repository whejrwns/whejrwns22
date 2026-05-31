def print_gugudan():
    # 콘솔 창 너비가 좁아 줄바꿈이 깨지는 것을 방지하기 위해 3개 단씩 끊어서 출력
    for start in range(1, 10, 3):
        end = min(start + 3, 10)
        
        # 단 제목 출력
        for i in range(start, end):
            print(f"   [{i}단]   ", end="    ")
        print()
        
        # 구구단 내용 가로로 출력
        for j in range(1, 10):
            for i in range(start, end):
                print(f"{i} x {j} = {i * j:2d}", end="    ")
            print()
        print() # 블록 구분을 위한 빈 줄

if __name__ == "__main__":
    print_gugudan()
