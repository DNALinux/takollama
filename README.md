# TakoLlama

A Python library for building Retrieval-Augmented Generation (RAG) systems with Ollama and ChromaDB. TakoLlama simplifies the process of extracting text from various sources, creating vector embeddings, and querying them with large language models.

## Features

- **Multi-format Text Extraction**: Extract text from PDFs, HTML files, and web URLs
- **Vector Database Management**: Built-in ChromaDB integration for efficient similarity search
- **Ollama Integration**: Seamless integration with Ollama for embeddings and text generation
- **Web Crawling**: Intelligent web crawling with relevance filtering
- **Flexible Data Processing**: Configurable text chunking with overlap for better context preservation

## Installation

```bash
pip install takollama
```

### Prerequisites

- Python 3.12+
- [Ollama](https://ollama.ai/) installed and running
- Required models pulled in Ollama (e.g., `ollama pull llama3.1`, `ollama pull mxbai-embed-large`)

## Quick Start

### 1. Basic RAG Pipeline

```python
from takollama import RAG, VectorDB

# Initialize the RAG system
rag = RAG(
    chroma_db_dir="./my_db",
    chroma_db_name="my_collection",
    v_model="mxbai-embed-large"
)

# Load data from PDFs and HTML files
rag.vector_db.load_data(input_dir="./documents")

# Query the system
answer = rag.generate_answer("What is machine learning?", model="llama3.1")
print(answer)
```

### 2. Working with URLs

```python
from takollama import VectorDB

# Initialize vector database
vdb = VectorDB("./web_db", "web_collection")

# Load data from URLs
vdb.load_data(urls_path="urls.txt")

# Query the database
results = vdb.query("How to install software?", k=5)
print(results)
```

### 3. Text Extraction Only

```python
from takollama import TextExtractor

# Initialize text extractor
extractor = TextExtractor(
    input_dir="./documents",
    output_dir="./extracted_text",
    urls_file="urls.txt"
)

# Extract from PDFs
pdf_files = extractor.get_pdf()
for pdf in pdf_files:
    texts = extractor.extract_pdf_texts(pdf)
    print(f"Extracted {len(texts)} chunks from {pdf}")

# Extract from web URLs
urls = extractor.get_urls()
for url in urls:
    chunks = extractor.crawl_and_extract(url, max_depth=2)
    print(f"Extracted {len(chunks)} chunks from {url}")
```

## Core Components

### RAG Class
The main interface for retrieval-augmented generation:
- `generate_answer(query, k=4, model="llama3.1")`: Generate answers using retrieved context
- `generate_prompt(question, context)`: Create prompts for the LLM

### VectorDB Class
Manages the vector database operations:
- `load_data(input_dir, output_dir, urls_path)`: Load data from various sources
- `query(query_text, k=5)`: Search for similar documents
- `show_sources()`: List all data sources in the database
- `delete_source(source)`: Remove documents from a specific source

### TextExtractor Class
Handles text extraction from multiple formats:
- `extract_pdf_texts(pdf_path)`: Extract text from PDF files
- `extract_html_text(html_path)`: Extract text from HTML files
- `crawl_and_extract(url, max_depth=1)`: Crawl websites and extract content

## Configuration

Create a `config.yaml` file for your project:

```yaml
vector_db:
  input_dir: "./data/documents/"
  output_dir: "./data/processed/"
  urls_path: "./data/urls.txt"
  chroma_db_dir: "./data/vector_db/"
  chroma_db_name: 'my_collection'
  model: "mxbai-embed-large"

ollama_model:
  model_name: "llama3.1"
```

## Advanced Usage

### Custom Text Chunking

```python
# Extract with custom chunk size and overlap
extractor = TextExtractor("./docs", "./output")
chunks = extractor.extract_html_text(
    "document.html", 
    chars_per_file=1000, 
    overlap=200
)
```

### Web Crawling with Depth Control

```python
# Crawl website with custom parameters
chunks = extractor.crawl_and_extract(
    "https://example.com",
    chunk_size=800,
    overlap_size=100,
    max_depth=3
)
```

### Database Management

```python
# Check database status
vdb = VectorDB("./db", "collection")
print(f"Documents in database: {vdb.count_docs()}")
print(f"Available sources: {vdb.show_sources()}")

# Clear database
vdb.clear_database()
```

## Supported Models

### Embedding Models
- `mxbai-embed-large` (recommended)
- `nomic-embed-text`

### Language Models

Any model supported by Ollama, like:

- `gpt-oss:20b`
- `deepseek-r1:8b`
- `gemma3:12b`
- `llama3.1`
- `llama3.2:3b`
- `llama3.3:70b`
- `phi4:14b`

## Examples

The package includes various example scripts in `takollama.scripts`:
- `RAG_query.py`: Command-line RAG querying (available as `takollama-query`)
- `extract_text.py`: Text extraction utility (available as `takollama-extract`)
- `create_rag_pipeline.py`: Pipeline creation examples
- `createDBlocal.py`: Local database creation
- `createDBColab.py`: Colab-specific database setup

The `notebooks/` directory contains Jupyter notebooks with detailed examples:
- `DNALinux_RAG_UV.ipynb`: Complete RAG workflow
- Various demonstration notebooks for different use cases

You can access these scripts after installation:
```python
# Access script utilities programmatically
from takollama.scripts import RAG_query, extract_text
```

## Command Line Tools

After installation, TakoLlama provides command-line tools for common tasks:

### Query RAG Database

```bash
takollama-query \
  --e_model mxbai-embed-large \
  --LLM_model llama3.1 \
  --db_dir ./my_db \
  --db_name my_collection \
  --query "Your question here" \
  --k 4
```

### Extract Text from Documents

```bash
# Extract from PDFs and HTML files
takollama-extract \
  --input_dir ./documents \
  --output_dir ./extracted_text \
  --process_pdfs \
  --process_html

# Extract from URLs
takollama-extract \
  --output_dir ./web_content \
  --urls_file urls.txt \
  --process_urls \
  --max_depth 2

# Extract from all sources
takollama-extract \
  --input_dir ./documents \
  --output_dir ./all_content \
  --urls_file urls.txt \
  --process_pdfs \
  --process_html \
  --process_urls \
  --chunk_size 800 \
  --overlap 150
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GPL 3.0 as specified in the LICENSE file.

## Requirements

- `bs4>=0.0.2`
- `chromadb>=1.0.17`
- `langchain-community>=0.3.27`
- `ollama>=0.5.3`
- `pypdf>=6.0.0`

## Support

For issues and questions, please use the GitHub issue tracker.