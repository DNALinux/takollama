"""
create a new DB

sample run:

createDBColab.py --db_dir mydb --db_name blastdb --e_llm nomic-embed-text --input_dir ../data/blastdb/

"""

#import os
#import sys
import argparse

#current_dir = os.path.dirname(os.path.abspath(__file__)) 
#target_dir = os.path.join(current_dir, '..') 
#sys.path.append(target_dir)
from takollama import VectorDB as vdb


parser = argparse.ArgumentParser(description='Create a database.')
parser.add_argument('--db_dir', type=str, required=True, 
    help='Path to where vector DB will be generated')
parser.add_argument('--db_name', type=str, required=True,  
    help='Name of the database')
parser.add_argument('--e_llm', type=str, default='nomic-embed-text', 
    help='Name of the vector LLM (default: nomic-embed-text)')
parser.add_argument('--input_dir', type=str, required=True, 
    help='Path to the input file')

# input_dir: "/content/ai/data/example_data

args = parser.parse_args()


db_dir = args.db_dir
db_name = args.db_name
#DBPATH = "/content/DBs/fornewDB/"
e_model = args.e_llm
input_dir = args.input_dir

print(f"Vector model: {e_model}")
t_vector_db = vdb(db_dir, db_name, e_model)
print("Current documents: ")
print(t_vector_db.count_docs())
t_vector_db.load_data(input_dir, "tmp")
#print(t_vector_db.collection_name)
print("Current documents: ")
print(t_vector_db.count_docs())

#test_vector_db.load_url()
print("**")

#print(urls_path)
