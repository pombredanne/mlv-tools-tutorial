#!/bin/bash -eux
pushd "$(git rev-parse --show-toplevel)"
DATA_FILE="./data/data_train_tokenized.csv"
RUN_UUID_FILE="./data/run_uuid.txt"
MODEL_FILE="./data/fasttext_model.bin"

dvc run \
-d $DATA_FILE \
-d $RUN_UUID_FILE \
-d $MODEL_FILE \
./scripts/python/evaluate --data-file $DATA_FILE --run-uuid-file $RUN_UUID_FILE --model-file $MODEL_FILE


popd