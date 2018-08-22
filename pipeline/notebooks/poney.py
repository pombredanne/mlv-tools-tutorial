# Generated from ./pipeline/notebooks/Load_with_sklearn.ipynb


def load_with_sklearn(subset='train'):


    import numpy as np
    import pandas as pd
    from sklearn.datasets import fetch_20newsgroups

    newsgroups_train = fetch_20newsgroups(subset=subset,
                                          remove=('headers', 'footers', 'quotes'))

    newsgroups_train.keys()

    len(newsgroups_train.data)

    newsgroups_train.target

    newsgroups_train.keys()

    df_train = pd.DataFrame(newsgroups_train.data, columns=['data'])

    df_train['target'] = newsgroups_train.target

    df_train['targetnames'] = df_train['target'].apply(lambda n: newsgroups_train.target_names[n])

    df_train.to_csv('data_train.csv', index=None)