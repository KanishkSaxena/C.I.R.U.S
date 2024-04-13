import pandas as pd
import os

def load_data_v1(data_dir, data_root):
    passages = pd.read_csv(os.path.join(data_root,data_dir, "passages.tsv"), sep='\t', header=0)
    qas = pd.read_csv(os.path.join(data_root,data_dir, "questions.tsv"), sep='\t', header=0).rename(columns={"text": "question"})
    
    return passages, qas
