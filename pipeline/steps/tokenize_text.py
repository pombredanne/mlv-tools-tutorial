# Generated from pipeline/notebooks/Tokenize_text.ipynb
    
    



def tokenize_text(input_csv_file:str, output_csv_file:str):

    """

    :param str input_csv_file: Path to input file

    :param str output_csv_file: Path to output file

    """



    import pandas as pd
    import numpy as np
    from nltk.tokenize import wordpunct_tokenize
    from nltk.corpus import stopwords

    df = pd.read_csv(input_csv_file)
    df.head()

    stopswords_english = set(stopwords.words('english'))

    def tokenize_and_clean_text(s):
        return [token.lower() for token in wordpunct_tokenize(s) if token.isalpha() and token.lower() not in stopswords_english]

    df = df.dropna()

    df['data'] = df['data'].apply(tokenize_and_clean_text)

    # No effect
    df.head()

    df.to_csv(output_csv_file, index=False)