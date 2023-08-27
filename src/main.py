import os
import argparse

class QuickProjectInit:
    def __init__(self, directory) -> None:
        self.directory = directory[0]

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
            os.chdir(folder)
            if not os.path.exists("README.md"):
                open("README.md", "a").close()

    def build_gitignore(self):
        os.chdir(self.directory)
        if not os.path.exists(".gitignore"):
            open(".gitignore", "a").close()

    def build_requirements(self):
        os.chdir(self.directory)
        if not os.path.exists("requirements.txt"):
            open("requirements.txt", "a").close()        

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

def parser():
    parser = argparse.ArgumentParser(
        prog="Quick Project Initialiser",
        description="QPI is a tool I created to save time when building a new project."
    )
    parser.add_argument(
        '-b', '--build', nargs=1, default=str(os.getcwd()), type=str)
    parser.add_argument(
        '-py', '--pysetup', nargs=1, default=False, type=bool
    )
    return parser.parse_args()

def main():
    args = parser()
    qpi = QuickProjectInit(args.build)
    qpi.build_folders()
    qpi.build_readme_files()
    qpi.build_gitignore()
    if args.pysetup:
        qpi.build_requirements()
        qpi.build_pyproject()

if __name__ == "__main__":
    main()