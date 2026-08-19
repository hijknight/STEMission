CORRECT_PASSWORD = "luminexus"
from game.display import login_success
def login():
    attempts = 0
    while True:
        username = input("USERNAME: ")
        password = input("PASSWORD: ").strip()

        if password.lower() == CORRECT_PASSWORD:
            print()
            print("ACCESS GRANTED")
            print()

            return username
        attempts += 1

        print()
        print("ACCESS DENIED")
        print()

        if attempts >= 2:
            print(f"Hint: Examine the physical evidence recovered from the labaratory.\n"
                  f" Does anything look especially out of place in the lab notebook?"
                )
            print()