# Generated from pipeline/notebooks/Fetch_dataset.ipynb
    
    



def fetch_dataset(target_directory:str, cache_path:str):

    """

    :param str target_directory: Download directory

    :param str cache_path: Path to cache file

    """



    from sklearn.datasets.twenty_newsgroups import download_20newsgroups

    buffer = download_20newsgroups(target_dir=target_directory, cache_path=cache_path)