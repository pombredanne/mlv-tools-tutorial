#!/bin/bash

pushd "$(git rev-parse --show-toplevel)"
dvc run -o ./data/20news-bydate_py3.pkz \
    ./scripts/python/fetch_dataset --target-directory ./data/20_newsgroup/ --cache-path ./data/20news-bydate_py3.pkz
 
popd
