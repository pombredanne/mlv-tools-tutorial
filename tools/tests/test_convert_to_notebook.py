import tempfile
from os.path import realpath, dirname, join, exists

from tools.ipynb2Python import export

CURRENT_DIR = realpath(dirname(__file__))


def test_should_convert_notebook_to_python_script():
    with tempfile.TemporaryDirectory() as tmp:
        output_path = join(tmp, 'out.py')
        export(input_notebook_path=join(CURRENT_DIR, 'data', 'test.ipynb'),
               output_path=output_path)

        assert exists(output_path)
        with open(output_path, 'r') as fd:
            content = fd.read()

        # Check main method is created
        assert 'def test():' in content


def test_should_detect_parameters():
    with tempfile.TemporaryDirectory() as tmp:
        output_path = join(tmp, 'out.py')
        export(
            input_notebook_path=join(CURRENT_DIR, 'data', 'test_param.ipynb'),
            output_path=output_path)

        assert exists(output_path)
        with open(output_path, 'r') as fd:
            content = fd.read()

        # Check main method is created
        assert 'def test_param(param1=3, param2=None):' in content


def test_should_be_resilient_to_empty_notebook():
    with tempfile.TemporaryDirectory() as tmp:
        output_path = join(tmp, 'out.py')
        export(
            input_notebook_path=join(CURRENT_DIR, 'data', 'test_empty.ipynb'),
            output_path=output_path)

        assert exists(output_path)

