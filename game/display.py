

def opening():
    print("""
╔═════════════════════════════════════════════════════════╗
║    ▞▀▖   ▌  ▐                           ▌     ▌         ║
║    ▚▄ ▌ ▌▛▀▖▜▀ ▞▀▖▙▀▖▙▀▖▝▀▖▛▀▖▞▀▖▝▀▖▛▀▖ ▌  ▝▀▖▛▀▖▞▀▘    ║
║    ▖ ▌▌ ▌▌ ▌▐ ▖▛▀ ▌  ▌  ▞▀▌▌ ▌▛▀ ▞▀▌▌ ▌ ▌  ▞▀▌▌ ▌▝▀▖    ║
║    ▝▀ ▝▀▘▀▀  ▀ ▝▀▘▘  ▘  ▝▀▘▘ ▘▝▀▘▝▀▘▘ ▘ ▀▀▘▝▀▘▀▀ ▀▀     ║
║                      MAINFRAME                          ║
║                                                         ║
║                AUTHENTICATION REQUIRED                  ║
║                                                         ║
╚═════════════════════════════════════════════════════════╝
""")


def username_success(username):
    if username == "ecarter1997":
        print("WELCOME BACK, DR. CARTER")
    elif username == "admin":
        print("WELCOME BACK, ADMIN")


def login_success():
    print("""
==============================================
    CONNECTION TO MAINFRAME ESTABLISHED
            =================          
Type 'help' to display available commands.
==============================================
""")