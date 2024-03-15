def calculate_volume(length,width,height):
    return length*width*height
def main():
    length = float(input("가로는:"))
    width = float(input("세로는:"))
    height = float(input("높이는:"))
    volume = calculate_volume(length, width, height)
    print("박스의 부피는", volume, "입니다.")
if __name__ == "__main__":
    main()
