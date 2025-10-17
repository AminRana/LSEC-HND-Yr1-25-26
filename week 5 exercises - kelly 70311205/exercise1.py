# Kelly Scott - 70311205

def a():
    def is_vowel(letter : str) -> bool:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u": return True
        return False

    string = input("Enter a word!\n")

    for letter in string:
        if is_vowel(letter):
            print(letter + " is a vowel!")
        else:
            print(letter + " is not a vowel!")

def b():
    total = 0
    for i in range(20):
        num = i + 1

        if num % 2 == 0:
            total += num

    print(total)

def c():
    def get_menu_input() -> int:
        print("1. Add\n"
              "2. Search\n"
              "3. Update\n"
              "4. Delete\n"
              "5. Quit")
        return int(input())

    user_input = get_menu_input()

    while user_input != 5:
        if user_input == 1:
            print("Added")
        elif user_input == 2:
            print("Searched")
        elif user_input == 3:
            print("Updated")
        elif user_input == 4:
            print("Deleted")

        user_input = get_menu_input()

        if user_input == 5:
            print("Bye!")

def d():
    def check_if_prime_number(num : int) -> bool:
        if num == 1:
            return False

        for i in range(1, num+1):
            if i != 1 and i != num:
                if num % i == 0:
                    return False

        return True

    num = int(input("Enter a number: "))

    is_prime = check_if_prime_number(num)

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is a composite number.")

def e():
    def check_if_prime_number(num : int) -> bool:
        if num == 1:
            return False

        for i in range(1, num+1):
            if i != 1 and i != num:
                if num % i == 0:
                    return False

        return True

    def get_all_prime_numbers(max : int) -> list:
        prime_numbers = []

        for i in range(1, max+1):
            if check_if_prime_number(i):
                prime_numbers.append(i)

        return prime_numbers

    u_input = int(input("Enter a max number: "))

    string = "Prime numbers: "

    for num in get_all_prime_numbers(u_input):
        string += str(num) + ", "

    print(string)

def f():
    num = int(input("Enter number: "))

    for i in range(1, 11):
        mult = num * i
        print(f"{num}x{i}={mult}")

# Kelly Scott - 70311205