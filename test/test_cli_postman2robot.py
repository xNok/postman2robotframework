import pytest
from shutil import copyfile
from shutil import copytree
import os

from cli.postman2robot import run as postman2robot

@pytest.fixture(scope="function")
def collection(tmpdir, request):

    if request.param:
        test_name = request.param
    else:
        test_name = request.node.name


    filepath = request.module.__file__
    test_dir, f = os.path.split(filepath)

    # Resolve paths
    resources = os.path.join(test_dir, "resources")
    resources_collection = os.path.join(resources, test_name + "_collection.json")
    resources_validation = os.path.join(resources, "validation" , test_name + "_library.py")

    # Prepare env
    copyfile(resources_collection, os.path.join(tmpdir, "collection.json"))
    copyfile(resources_validation, os.path.join(tmpdir, "validation_library.py"))

    # We work in temps dir
    old_cwd = os.getcwd()
    os.chdir(tmpdir)

    library = tmpdir.join('./postman_libraries/newmanTest.py')
    library_validation = tmpdir.join('./validation_library.py')

    yield {"generated": library, "expected": library_validation}

    os.chdir(old_cwd)
 
class Test_Postman2Robot:

    cli_args = {
        "--ifile": "collection.json",
        "--ofile": "./postman_libraries"
    }

    @pytest.mark.parametrize("collection", [("test_simple")], indirect=True)
    def test_simple(self, tmpdir, collection):
        """
        Given collection.json, generate: library.py
        """

        postman2robot(self.cli_args)

        assert os.path.isfile(collection["generated"])
        assert collection["generated"].read() == collection["expected"].read()