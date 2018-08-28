#!/bin/bash

pushd "$(git rev-parse --show-toplevel)"
dvc run -d ./data/data_train.csv \
    -o ./data/data_train_tokenized.csv \
    ./scripts/python/tokenize_text --input-csv-file ./data/data_train.csv  --output-csv-file ./data/data_train_tokenized.csv
popd