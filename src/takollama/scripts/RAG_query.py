"""
TakoLlama RAG Query Script

Usage:
takollama-query --e_model mxbai-embed-large --LLM_model phi4 --db_dir /path/to/db/ --db_name mydb --query "Your question here"

Embedding models:
- nomic-embed-text
- mxbai-embed-large

LLM Models:
- llama3.1
- llama3.2:3b
- llama3.3:70b
- phi4
"""
import argparse
from takollama import RAG


def main():
    parser = argparse.ArgumentParser(description='Query a RAG database using TakoLlama.')
    parser.add_argument('--e_model', type=str, required=False, 
                        default='mxbai-embed-large', help='Vector Model (default: mxbai-embed-large)')
    parser.add_argument('--LLM_model', type=str, required=False, 
                        default='llama3.1', help='LLM Model (default: llama3.1)')
    parser.add_argument('--db_dir', type=str, required=True, 
        help='Path to the database directory')
    parser.add_argument('--db_name', type=str, required=True,  
        help='Name of the database collection')
    parser.add_argument('--query', type=str, required=True,  
        help='Query to ask the RAG system')
    parser.add_argument('--k', type=int, default=4,
        help='Number of documents to retrieve (default: 4)')

    args = parser.parse_args()

    print(f"Embedding model: {args.e_model}")
    print(f"LLM: {args.LLM_model}")
    print(f"Database: {args.db_dir}/{args.db_name}")
    print(f"Query: {args.query}")
    print("-" * 50)

    try:
        # Initialize RAG system
        rag_system = RAG(args.db_dir, args.db_name, v_model=args.e_model)
        
        # Generate answer
        answer = rag_system.generate_answer(args.query, k=args.k, model=args.LLM_model)
        
        print("Answer:")
        print(answer)
        print("-" * 50)
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())

