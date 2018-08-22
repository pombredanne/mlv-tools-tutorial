#!/usr/bin/env python3
import argparse
import logging
from os import makedirs
from os.path import abspath
from os.path import realpath, dirname, join, basename

from nbconvert import PythonExporter

logging.getLogger().setLevel(logging.INFO)
CURRENT_DIR = realpath(dirname(__file__))
TEMPLATE_PATH = join(CURRENT_DIR, 'template', 'ml-python.pl')


def get_config(template_path: str) -> dict:
    return {'TemplateExporter': {'template_file': template_path},
            'NbConvertApp': {'export_format': 'python'}}


def export(input_notebook_path: str, output_path: str):
    exporter = PythonExporter(get_config(TEMPLATE_PATH))

    output_script, r = exporter.from_filename(input_notebook_path)
    if not output_script:
        logging.warning('Empty notebook provided. Nothing to do.')
        return
    makedirs(dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as fd:
        fd.write(output_script)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Notebook to python '
                                                 'script')
    parser.add_argument('-n', '--notebook', type=str, required=True,
                        help='The notebook to convert')
    parser.add_argument('-o', '--output', type=str,
                        help='The Python script output path')
    args = parser.parse_args()

    output_path = args.output
    if not output_path:
        script_name = '{}.py'.format(
            basename(args.notebook).replace('.ipynb', '')
            .replace(' ', '_')
            .lower())
        output_path = join(CURRENT_DIR, '..', 'pipeline', 'steps', script_name)

    export(args.notebook, output_path)
    logging.info(f'Python script generated in {abspath(output_path)}')
