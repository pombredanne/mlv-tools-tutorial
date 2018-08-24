# POC versioning Machine Learning pipeline

Exploration of a text classification task on 20newsgroup dataset

The use-cases to consider are the following:
- Hyperparameter optimisation and fine-tuning (saving results)
- Versioning and storage of intermediate (preprocessed) datasets; partial execution of the pipeline starting from precomputed data
- Reproduce a pipeline / experience on new data

Proposed test pipeline:
1. 
    a. Raw text -> tokenizing and cleaning -> clean_data_1 (Preprocessing 1)
    
    b. Raw text -> tokeninzing and lemmatisation and cleaning -> clean_data_2 (Preprocessing 2)
2. 
    a. Clean data -> Bag-of-word (hyperparameter: vocabulary size) -> encoded data
    
    b. Clean data -> Word Embedding -> encoded data
    
    c. Clean data -> fastText -> labels
3. 
    a. Encoded data -> Random Forests (hyperparameters: a lot) -> labels
    
    b. Logisitic Regression -> labels
    
    c. Latent Dirichlet Allocation -> labels


## Standard versioning process
   
   1. Write a **Jupyter Notebook** which correspond to a pipeline step (See **Jupyter Notebook** syntax section)
   2. Test your **Jupyter Notebook**
   3. Clean output and add it under git (TODO hooks)
   3. Convert the **Jupyter Notebook** into a parameterized **Python 3** script using *ipynb_to_python*
       
            ipynb_to_python -n ./pipeline/notebooks/[notebook_name] -o ./pipeline/steps/[python_script_name]
   4. Ensure python script is well created into `./pipeline/steps/[python_script_name]`
   5. Create python command associated to to generated parameterized **Python 3** script
   
            script_to_cmd -i ./pipeline/steps/[python_script_name] \
                        --out-py-cmd ./scripts/python/[python_cmd_name] \
                        --out-bash-cmd ./scripts/cmd/[dvc_cmd_name] 
                        
   6. Ensure **Python 3** command is well created
            
            ./scripts/python/[python_cmd_name] -h
            
   7. Ensure **DVC** command is well created
   8. Add generated commands and **Python 3** script under git
   9. Add step inputs under dvc
   10. Run dvc command `./scripts/cmd/[dvc_cmd_name]`
   11. Add generated dvc files under git 
   


## Preliminary step: create project structure

    cd ml-poc-versioning
    git checkout -b [TODO put a ref commit ]
    
    mkdir -p pipeline/notebooks
    mkdir -p pipeline/steps
    touch pipeline/__init__.py
    touch pipeline/steps/__init__.py
    mkdir -p scripts/python
    mkdir -p scripts/cmd
    
Following structure must be created

    .
    ├── pipeline
    │   ├── notebooks # contains Jupyter Notebook (One by pipeline step)
    │   └── steps     # contains generated python script (obtained from Jupyter Notebook convertion)
    └── scripts
        ├── cmd       # contains dvc command wrapped in a bash script
        └── python    # contains python command which wrapped python script
        

    
     

## First step: loading data

Fetch data from [20_newsgroup](http://scikit-learn.org/stable/datasets/twenty_newsgroups.html).

*Output:* train and test csv files (`./data/data_train.csv` and `./data/data_test.csv`)

1. Write first step (data loading) in a notebook
2. Export to .py script (for now using Jupyter export function; TODO get a better solution)
3. Modify script by hand to get out the parameters (TODO: clean this dirty hack)
4. Initialize git and DVC repo
5. Version empty notebook and hand-written script
6. Run DVC on script to version data results
