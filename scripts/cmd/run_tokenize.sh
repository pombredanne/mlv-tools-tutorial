#!/bin/bash

pushd "$(git rev-parse --show-toplevel)"
dvc run -d ./data/data_train.csv \
        -o ./data/data_train_tokenized.csv \
        python ./scripts/python/tokenize_text.py -i ./data/data_train.csv
popd
