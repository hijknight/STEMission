from pathlib import Path

from game.authentication import login
from game.display import login_success, opening
from game.filesystem import FakeFileSystem
from game.terminal import Terminal

def main():

    project_root = Path(__file__).parent

    game_files = project_root / "game_files"

    filesystem = FakeFileSystem(game_files)

    while True:
        filesystem.reset()

        opening()

        username = login()

        login_success(username)

        terminal = Terminal(filesystem)

        terminal.run(username)


if __name__ == '__main__':
    main()