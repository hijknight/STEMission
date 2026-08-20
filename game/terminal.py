from game.printer import print_file

class Terminal:
    def __init__(self, filesystem):
        self.filesystem = filesystem
        self.running = True
        #self.print = print

        self.commands = {
            "help": self.command_help,
            "ls": self.command_ls,
            "pwd": self.command_pwd,
            "cd": self.command_cd,
            "view": self.command_view,
            "clear": self.command_clear,
            "logout": self.command_logout,
            "print": self.command_print,
            "unlock":self.command_unlock,
        }

    def run(self, username):
        while self.running:
            path = self.filesystem.get_path()

            command_line = input(
                f"{username}@subterranean:{path}> "
            ).strip()

            if not command_line:
                continue
            self.execute(command_line)

    def execute(self, command_line):

        parts = command_line.split(maxsplit=1)

        command_name = parts[0].lower()

        argument = ""

        if len(parts) > 1:
            argument = parts[1]

        command = self.commands.get(command_name)

        if command is None:
            print(
                f"Unknown command: {command_line}\n"
                "Type 'help' to see available commands"
            )
            return
        command(argument)

    def command_help(self, argument):
        print("""
AVAILABLE COMMANDS

help              Show available commands
ls                List files
pwd               Show current directory
cd <directory>    Change directory
view <file>       Read a file
unlock <file>     Unlock a protected file
print <file>      Print a specified file (very helpful)
clear             Clear the terminal
logout            Log out
""")

    def command_ls(self, argument):
        self.filesystem.ls()

    def command_pwd(self, argument):
        print(self.filesystem.get_path())

    def command_cd(self, argument):
        if not argument:
            print("Usage: cd <directory>")
            return

        self.filesystem.cd(argument)

    def command_view(self, argument):
        if not argument:
            print("Usage: view <filename>")
            return
        self.filesystem.view(argument)

    def command_clear(self, argument):
        print("\033[2J\033[H", end="")

    def command_logout(self, argument):

        print("\033[2J\033[H", end="")
        self.running = False

    def command_print(self, argument):

        if not argument:
            print("Usage: print <filename>")
            return

        file_path = self.filesystem.get_real_file_path(argument)
        print(file_path)

        if file_path is None:
            print(f"File not found: {argument}")
            return

        print()
        print("CENTRAL PRINT SERVICE")
        print("---------------------")
        print(f"Document: {argument}")
        print("Submitting print job...")


        if print_file(file_path):
            print("PRINT JOB ACCEPTED")
        else:
            print("PRINT JOB FAILED")

        print()

    def command_unlock(self, argument):
        if not argument:
            print("Usage: unlock <filename>")
            return

        password = input("PASSWORD: ").strip()

        self.filesystem.unlock(
            argument,
            password
        )