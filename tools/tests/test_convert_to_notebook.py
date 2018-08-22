import tempfile
from os.path import realpath, dirname, join, exists

import nbformat as nbf
import pytest

from tools.ipynb2Python import export

CURRENT_DIR = realpath(dirname(__file__))


def gen_notebook(nb_cells: int, tmp_dir: str, file_name: str,
                 docstring: str = None):
    nb = nbf.v4.new_notebook()
    if docstring:
        nb['cells'].append(nbf.v4.new_code_cell(docstring))
    for i in range(nb_cells):
        nb['cells'].append(nbf.v4.new_code_cell('print(\'poney\')'))
    notebook_path = join(tmp_dir, file_name)
    nbf.write(nb, notebook_path)
    return notebook_path


def test_should_convert_notebook_to_python_script():
    with tempfile.TemporaryDirectory() as tmp:
        output_path = join(tmp, 'out.py')
        notebook_path = gen_notebook(nb_cells=1, tmp_dir=tmp,
                                     file_name='test.ipynb', docstring=None)
        export(input_notebook_path=notebook_path, output_path=output_path)

        assert exists(output_path)
        with open(output_path, 'r') as fd:
            content = fd.read()

        # Check main method is created
        assert 'def test():' in content


def test_should_detect_parameters():
    with tempfile.TemporaryDirectory() as tmp:
        output_path = join(tmp, 'out.py')

        docstring_cell = '''
        # Parameters
        """
            :param str subset: The kind of subset to generate.
            :param int rate: The rate of I don't know what 
            :param param3:
        """
        subset = 'train'
        toto = 12
        '''

        notebook_path = gen_notebook(nb_cells=1, tmp_dir=tmp,
                                     file_name='test.ipynb',
                                     docstring=docstring_cell)
        export(input_notebook_path=notebook_path, output_path=output_path)
        assert exists(output_path)
        with open(output_path, 'r') as fd:
            content = fd.read()

        # Check main method is created
        assert 'def test(subset:str, rate:int, param3):' in content

def test_should_raise_if_invalid_docstring():
    with tempfile.TemporaryDirectory() as tmp:
        output_path = join(tmp, 'out.py')

        docstring_cell = '''
        # Parameters
        """
            :param param3
        """
        subset = 'train'
        toto = 12
        '''

        notebook_path = gen_notebook(nb_cells=1, tmp_dir=tmp,
                                     file_name='test.ipynb',
                                     docstring=docstring_cell)
        with pytest.raises(Exception):
            export(input_notebook_path=notebook_path, output_path=output_path)

def test_should_raise_if_more_than_one_docstring_in_first_cell():
    with tempfile.TemporaryDirectory() as tmp:
        output_path = join(tmp, 'out.py')

        docstring_cell = '''
        # Parameters
        """
            :param param3: Plop
        """
         """
            :param param6: AA
        """
        subset = 'train'
        toto = 12
        '''

        notebook_path = gen_notebook(nb_cells=1, tmp_dir=tmp,
                                     file_name='test.ipynb',
                                     docstring=docstring_cell)
        with pytest.raises(Exception):
            export(input_notebook_path=notebook_path, output_path=output_path)

def test_should_be_resilient_to_empty_notebook():
    with tempfile.TemporaryDirectory() as tmp:
        output_path = join(tmp, 'out.py')
        notebook_path = gen_notebook(nb_cells=0, tmp_dir=tmp,
                                     file_name='test.ipynb',docstring=None)
        export(input_notebook_path=notebook_path, output_path=output_path)
        assert exists(output_path)
