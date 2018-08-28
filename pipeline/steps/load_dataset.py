# Generated from pipeline/notebooks/Load_with_sklearn.ipynb
    
    



def load_with_sklearn(subset:str, data_home:str, output_path:str):

    """

    :param str subset: Subset of data to load

    :param str data_home: Path to parent directory to cache file

    :param str output_path: Path to output file

    """



    import numpy as np
    import pandas as pd
    from sklearn.datasets import fetch_20newsgroups

    newsgroups_train = fetch_20newsgroups(subset=subset,
                                          data_home=data_home,
                                          download_if_missing=False,
                                          remove=('headers', 'footers', 'quotes'))

    # No effect
    newsgroups_train.keys()

    # No effect
    len(newsgroups_train.data)

    # No effect
    newsgroups_train.target

    df_train = pd.DataFrame(newsgroups_train.data, columns=['data'])

    df_train['target'] = newsgroups_train.target

    df_train['targetnames'] = df_train['target'].apply(lambda n: newsgroups_train.target_names[n])

    # No effect
    df_train.head()

    df_train.to_csv(output_path, index=None)