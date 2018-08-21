#!/usr/bin/env python3
import argparse
import logging
import sys
from argparse import FileType
from Tokenize_text import tokenize_dataset


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tokenize and clean dataset')
    parser.add_argument('-i', '--input', type=str,
                        help='Input file', required=True)
    args = parser.parse_args()
    tokenize_dataset(args.input)
