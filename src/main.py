__author__ = "Aryn Taylor"
__email__ = "aryntaylor2021@gmail.com"
__version__ = "v1.0.0"
__project__ = "Quick Project Initialiser"
__copyright__ = f"© 2023 By {__author__}"

import os
import argparse


class QuickProjectInit:
    def __init__(self, directory) -> None:
        self.directory = directory

    def build_folders(self):
        folders = ["src", "tests"]
        os.chdir(self.directory)

        for folder in folders:

            if not os.path.exists(folder):
                os.mkdir(folder)

    def build_readme_files(self):
        folders = ["src","tests",self.directory]

        for folder in folders:
            os.chdir(self.directory)

            if not os.path.exists(folder):
                return False

            os.chdir(folder)

            if not os.path.exists("README.md"):
                open("README.md", "a").close()

        os.chdir(self.directory)

    def build_gitignore(self):
        os.chdir(self.directory)
        if not os.path.exists(".gitignore"):
            open(".gitignore", "a").close()

    def build_requirements(self):
        os.chdir(self.directory)

        if not os.path.exists("requirements.txt"):
            with open("requirements.txt", "a") as file:
                content = [
                    "setuptools >= 21.0.0"
                    ]

    def build_pyproject(self):
        os.chdir(self.directory)

        if not os.path.exists("pyproject.toml"):
            with open("pyproject.toml", "a") as file:
                content = [
                    '[project]',
                    'name = "project_name"',
                    'description = "description"',
                    'version = "1.1.0"',
                    '',
                    '[build-system]',
                    'requires = ["setuptools>=61.0"]',
                    'build-backend = "setuptools.build_meta"',
                    '',
                    '[tool.setuptools.packages.find]',
                    'where = ["src"]',
                    '',
                    '[tool.pytest.ini_options]',
                    'pythonpath = [',
                    '    ".", "src", "tests"',
                    ']'
                ]
                file.writelines(line + "\n" for line in content)

    def build_pyfiles(self):
        folders = ["src", "tests"]

        for folder in folders:
            os.chdir(self.directory)

            if not os.path.exists(folder):
                return False

            os.chdir(folder)

            if not os.path.exists("__init__.py"):
                open("__init__.py", "a").close()

            if folder == "src":
                if not os.path.exists("main.py"):
                    open("main.py", "a").close()
            elif folder == "tests":
                if not os.path.exists("test_main.py"):
                    open("test_main.py", "a").close()

        os.chdir(self.directory)


def parser():
    def dir_path(string):
        if os.path.isdir(string):
            return string
        else:
            print("Path must be valid!")
            return None

    parser = argparse.ArgumentParser(
        prog="Quick Project Initialiser",
        description="QPI saves time by initiating new project files."
    )
    parser.add_argument(
        '-v', '--version', action="store_true")
    parser.add_argument(
        '-b', '--build', nargs=1, default=str(os.getcwd()), type=dir_path)
    parser.add_argument(
        '-py', '--pysetup', action="store_true")
    return parser.parse_args()

def display_version():
    header_line = ""
    for char in __project__:
        header_line += "-"
    print(header_line)
    print(__project__)
    print(__copyright__)
    print(__email__)
    print(__version__)
    print(header_line)

def main():
    args = parser()
    version = args.version
    directory = args.build

    if version:
        display_version()
        return True

    if isinstance(directory, list):
        directory = args.build[0]

    if not directory:
        return False

    qpi = QuickProjectInit(directory=directory)
    qpi.build_folders()
    qpi.build_readme_files()
    qpi.build_gitignore()

    if args.pysetup:
        qpi.build_requirements()
        qpi.build_pyproject()
        qpi.build_pyfiles()

    print(f"Successfully built project at: '{directory}'")

if __name__ == "__main__":
    main()
