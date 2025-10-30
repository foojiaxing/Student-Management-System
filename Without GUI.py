import random

username = ["howjieying", "foojiaxing", "ngkaylyn",
                 "chanyuanlin", "cherlywongexing", "siowqifeng",
                 "chongyuanwei", "gohsiying", "lavaniaachandramohan",
                 "nurulhumaidahsherin"]
password = ["1002371013", "1002371198", "1002372193", "1002371497",
                 "1002371070", "1002371213", "1002372877", "1002371454",
                 "1002372380", "1002370878"]

# Dictionary to hold username-password pairs
user_credentials = {}

# Assign usernames to passwords
for i in range(len(username)):
    user_credentials[username[i]] = password[i]


def generate_tac():
    return random.randint(100, 999)


def display_options():
    print("\nBanking options available:")
    print("-Transfer Top-up")
    print("-Make payments")
    print("-Receive money")


def main():
    attempts = 0
    while attempts < 3:
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user in user_credentials and user_credentials[user] == pwd:
            tac = generate_tac()
            print(f"TAC generated: {tac}")
            tac_input = int(input("Enter the TAC: "))

            if tac_input == tac:
                print("Customer validated successfully.")
                display_options()
            else:
                print("Invalid TAC. Exiting...")
            return

        else:
            attempts += 1
            print("Invalid username or password.")

    print("Invalid user. Exiting...")


if __name__ == "__main__":
    main()
