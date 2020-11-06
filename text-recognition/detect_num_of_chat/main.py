from _666718347 import Highlight

def main():
    game = Highlight.extract_highlight()
    frame_num = input("please enter 30 or 60 or sec: ")
    if(frame_num == "30" or frame_num == "60"):
        print("출력 프레임 단위: ", frame_num)
    elif(frame_num == "sec"):
        print("초 단위로 출력합니다")
    game.extract_highlight_section(frame_num)

if __name__ == '__main__':
    main()