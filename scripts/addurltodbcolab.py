"""
This will create a DB if it does not exists. If exists, 
it will use it to load it with data from a list of URLs

sample run in Colab:

!export DBDIR="/content/ai/data/raw/urls/index.urls" ; \
export DBN="blastdb" ; \
export VECTOR="nomic-embed-text" ; \
export INDIR="/content/ai/data/example_data/" ; \
/content/miniforge3/envs/ml/bin/python ai/scripts/addurltodbcolab.py \
--db_dir $DBDIR --db_name $DBN --v_llm $VECTOR --url_input_file $INDIR

"""

import argparse
from takollama import VectorDB as vdb


parser = argparse.ArgumentParser(description='Create a database.')
parser.add_argument('--db_dir', type=str, required=True, 
    help='Path to the input file')
parser.add_argument('--db_name', type=str, required=True,  
    help='Name of the database')
parser.add_argument('--e_llm', type=str, default='nomic-embed-text', 
    help='Name of the vector LLM (default: nomic-embed-text)')
parser.add_argument('--url_input_file', type=str, required=True, 
    help='Path to the input file')

args = parser.parse_args()
db_dir = args.db_dir
db_name = args.db_name
e_model = args.e_llm
url_input_file = args.url_input_file

print(f"Vector model: {e_model}")
t_vector_db = vdb(db_dir, db_name, e_model)
print("Current documents: ")
print(t_vector_db.count_docs())
t_vector_db.load_url(url_input_file)
print("Current documents: ")
print(t_vector_db.count_docs())

