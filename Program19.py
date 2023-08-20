def countdigit(no):
    count = 0
    while (no != 0):
        no = no//10
        count = count + 1
    return count




def main():
    print("Enter the number:")
    num = int(input())

    count = countdigit(num)
    print(count)

if __name__ == "__main__":
    main()  