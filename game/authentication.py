from game.display import username_success

CORRECT_PASSWORDS = ["cells4l", "battery", "bridgesarecool"]
POSSIBLE_USERNAMES = ["ecarter1997", "admin"]
def login():
    attempts = 0
    while True:
        username = input("USERNAME: ")

        if username in POSSIBLE_USERNAMES:
            username_success(username.lower())

        print("Please input your password...")
        print()
        password = input("PASSWORD: ").strip()



        if password.lower() in CORRECT_PASSWORDS:
            print()
            print("ACCESS GRANTED")
            print()

            return username, password
        attempts += 1

        print()
        print("ACCESS DENIED")
        print()

        if attempts >= 2:
            print(f"Hint: Examine the physical evidence recovered from the labaratory.\n"
                  f" Does anything look especially out of place in the lab notebook?"
                )
            print()