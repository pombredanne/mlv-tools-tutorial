#!/usr/bin/env python3
import argparse
import logging
import sys
from argparse import FileType
from Load_with_sklearn import load_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Load 20newsgroup data from sklearn')
    args = parser.parse_args()
    load_data(option='train')
    load_data(option='test')   
