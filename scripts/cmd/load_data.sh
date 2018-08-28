#!/bin/bash

pushd "$(git rev-parse --show-toplevel)"
dvc run -d ./data/20news-bydate_py3.pkz \
    -o ./data/data_train.csv \
    -o ./data/data_test.csv \
    ./scripts/python/load_dataset --data-home ./data/ --subset train --output-path ./data/data_train.csv  && \
    ./scripts/python/load_dataset --data-home ./data/ --subset test --output-path ./data/data_test.csv  
popd
