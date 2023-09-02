import pytest
import os
import shutil
from src.main import QuickProjectInit

@pytest.fixture(scope="session")
def directory():
    print("<==========[setup]==========>")
    root = os.path.abspath(os.path.dirname(__file__))
    if not os.path.exists(f"{root}/tmp"):
        os.mkdir(f"{root}/tmp")
    yield f"{root}/tmp"

    def teardown():
        print("<==========[teardown]==========>")
        shutil.rmtree(f"{root}/tmp/src")
        shutil.rmtree(f"{root}/tmp/tests")
        for file in os.listdir(f"{root}/tmp"):
            os.remove(f"{root}/tmp/{file}")

    teardown()

@pytest.fixture
def qpi(directory):
    return QuickProjectInit(directory)


class TestQuickProjectInit:
    def test_build_folders(self, qpi, directory):
        qpi.build_folders()
        assert os.path.exists(f"{directory}/src")
        assert os.path.exists(f"{directory}/tests")

    def test_build_readme_files(self, qpi, directory):
        qpi.build_readme_files()
        assert os.path.exists(f"{directory}/src/README.md")
        assert os.path.exists(f"{directory}/tests/README.md")
        assert os.path.exists(f"{directory}/README.md")

    def test_build_gitignore(self, qpi, directory):
        qpi.build_gitignore()
        assert os.path.exists(f"{directory}/.gitignore")

class TestPysetup:
    def test_build_requirements(self, qpi, directory):
        qpi.build_requirements()
        assert os.path.exists(f"{directory}/requirements.txt")

    def test_build_pyproject(self, qpi, directory):
        qpi.build_pyproject()
        assert os.path.exists(f"{directory}/pyproject.toml")

    def test_build_pyfiles(self, qpi, directory):
        qpi.build_pyfiles()
        assert os.path.exists(f"{directory}/src/main.py")
        assert os.path.exists(f"{directory}/tests/test_main.py")
