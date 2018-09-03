# Generated from pipeline/notebooks/FastText.ipynb
def fasttext(input_csv_file: str, model_path: str, learning_rate: float, epochs: int):
    """
    :param str input_csv_file: Path to input file
    :param str model_path: Path to model files
    :param float learning_rate: Learning rate
    :param int epochs: Number of epochs
    :dvc-cmd: dvc run -d ./data/data_train_tokenized.csv  -o ./data/fasttext_model.bin ./scripts/python/classify --learning-rate 0.7 --epochs 10 --input-csv-file ./data/data_train_tokenized.csv  --model-path  ./data/fasttext_model 
    """

    import pandas as pd
    import numpy as np
    from nltk import ngrams
    from pyfasttext import FastText
    import tempfile
    import os
    
    df = pd.read_csv(input_csv_file)
    
    import json
    df['data'] = df['data'].apply(lambda s: json.loads(s.replace("'", '"')))
    
    trigrams_set = [(label, trigram) 
                    for (label, words) in df[['targetnames', 'data']].itertuples(index=False, name=None)
                    if len(words) >= 3
                    for trigram in ngrams(words, 3)]
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = os.path.join(tmp_dir, 'trigrams')
        with open(tmp_path, 'w') as f:
            for label, words in trigrams_set:
                f.write('__label__{} {}\n'.format(label, ' '.join(words)))
        model = FastText()
        model.supervised(input=tmp_path, output=model_path, epoch=epochs, lr=learning_rate)
    