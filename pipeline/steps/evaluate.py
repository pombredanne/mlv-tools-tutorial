# Generated from pipeline/notebooks/Evaluate.ipynb
def evaluate(model_file: str, data_file: str, run_uuid_file: str):
    """
    :param str model_file: Path to model file
    :param str data_file: Path to data files
    :param str run_uuid_file: Path to file for storing run uuid
    :dvc-in data_file: ./data/data_train_tokenized.csv 
    :dvc-in run_uuid_file: ./data/run_uuid.txt 
    :dvc-in model_file: ./data/fasttext_model.bin 
    """

    import pandas as pd
    import numpy as np
    from nltk import ngrams
    from pyfasttext import FastText
    import json
    import mlflow
    
    df = pd.read_csv(data_file)
    df['data'] = df['data'].apply(lambda s: ' '.join(json.loads(s.replace("'", '"'))))
    
    model = FastText()
    model.load_model(model_file)
    
    with open(run_uuid_file) as file_desc:
        run_uuid = file_desc.read()
    
    predicted = pd.DataFrame(model.predict([sentence + '\n' for sentence in df['data']]), columns=['targetnames'])
    
    accuracy = ((predicted != df[['targetnames']]).sum() / len(df)).iloc[0]
    
    with mlflow.start_run(run_uuid=run_uuid):
        mlflow.log_metric('accuracy', accuracy)
    