#!/bin/bash -eux
pushd "$(git rev-parse --show-toplevel)"

dvc run -d ./data/data_train_tokenized.csv  -o ./data/fasttext_model.bin -o ./data/run_uuid.txt ./scripts/python/classify --learning-rate 0.7 --epochs 10 --input-csv-file ./data/data_train_tokenized.csv  --model-path  ./data/fasttext_model --run-uuid-file  ./data/run_uuid.txt


popd