class Terminal:
    def __init__(self, filesystem):
        self.filesystem = filesystem
        self.running = True

        self.commands = {
            "help": self.command_help,
            "ls": self.command_ls,
            "pwd": self.command_pwd,
            "cd": self.command_cd,
            "view": self.command_view,
            "clear": self.command_clear,
            "logout": self.command_logout,
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
view <file>        Read a file
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
