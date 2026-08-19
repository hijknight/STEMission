def opening():
    print("""
╔══════════════════════════════════════════════╗
║                                              ║
║             SUBTERRANEAN LABS                ║
║                                              ║
║                 MAINFRAME                    ║
║                                              ║
║          AUTHENTICATION REQUIRED             ║
║                                              ║
╚══════════════════════════════════════════════╝
""")


def login_success(username):
    if username == "ecarter1997":
        print("""
==============================================
          CONNECTION ESTABLISHED
            =================          
         WELCOME BACK, DR. CARTER
==============================================

Type 'help' to display available commands.

==============================================
""")
    elif username == "admin":
        print("""
==============================================
          CONNECTION ESTABLISHED
            =================          
         WELCOME BACK, ADMIN
==============================================

Type 'help' to display available commands.

==============================================
""")
    else:
        print("""
==============================================
          CONNECTION REJECTED         
==============================================
            UNKNOWN USER
""")
