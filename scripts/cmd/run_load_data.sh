#!/bin/bash

pushd "$(git rev-parse --show-toplevel)"
dvc run -d ./data \
        -o ./data/data_train.csv \
        -o ./data/data_test.csv \
        python ./scripts/python/load_sklearn_data.py
popd
