"""
TakoLlama Text Extraction Script

Usage:
takollama-extract --input_dir /path/to/docs --output_dir /path/to/output --urls_file urls.txt
"""
import argparse
from pathlib import Path
from takollama import TextExtractor


def main():
    parser = argparse.ArgumentParser(description='Extract text from PDFs, HTML files, and URLs using TakoLlama.')
    parser.add_argument('--input_dir', type=str, 
        help='Directory containing PDF and HTML files to process')
    parser.add_argument('--output_dir', type=str, required=True,
        help='Directory to save extracted text files')
    parser.add_argument('--urls_file', type=str, default='urls.txt',
        help='File containing URLs to crawl (default: urls.txt)')
    parser.add_argument('--chunk_size', type=int, default=500,
        help='Size of text chunks in characters (default: 500)')
    parser.add_argument('--overlap', type=int, default=100,
        help='Overlap between chunks in characters (default: 100)')
    parser.add_argument('--max_depth', type=int, default=1,
        help='Maximum crawling depth for URLs (default: 1)')
    parser.add_argument('--process_pdfs', action='store_true',
        help='Process PDF files in input directory')
    parser.add_argument('--process_html', action='store_true',
        help='Process HTML files in input directory')
    parser.add_argument('--process_urls', action='store_true',
        help='Process URLs from urls file')

    args = parser.parse_args()

    # Validate arguments
    if not any([args.process_pdfs, args.process_html, args.process_urls]):
        print("Error: You must specify at least one processing option (--process_pdfs, --process_html, or --process_urls)")
        return 1

    if (args.process_pdfs or args.process_html) and not args.input_dir:
        print("Error: --input_dir is required when processing PDFs or HTML files")
        return 1

    # Create output directory if it doesn't exist
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        # Initialize TextExtractor
        extractor = TextExtractor(
            input_dir=args.input_dir or "",
            output_dir=args.output_dir,
            urls_file=args.urls_file
        )

        # Process PDFs
        if args.process_pdfs:
            print("Processing PDF files...")
            pdf_files = extractor.get_pdf()
            if pdf_files:
                extractor.save_pdfs_texts(pdf_files)
                print(f"Processed {len(pdf_files)} PDF files")
            else:
                print("No PDF files found in input directory")

        # Process HTML files
        if args.process_html:
            print("Processing HTML files...")
            html_files = extractor.get_html()
            if html_files:
                extractor.save_html_texts(html_files)
                print(f"Processed {len(html_files)} HTML files")
            else:
                print("No HTML files found in input directory")

        # Process URLs
        if args.process_urls:
            print("Processing URLs...")
            urls = extractor.get_urls()
            if urls:
                for url in urls:
                    print(f"Crawling: {url}")
                    extractor.crawl_and_save(
                        url, 
                        chunk_size=args.chunk_size,
                        overlap_size=args.overlap,
                        max_depth=args.max_depth
                    )
                print(f"Processed {len(urls)} URLs")
            else:
                print(f"No URLs found in {args.urls_file}")

        # Clean up single-line files
        print("Cleaning up single-line files...")
        extractor.delete_oneline_files()

        print(f"Text extraction completed! Output saved to: {args.output_dir}")
        
    except Exception as e:
        print(f"Error during text extraction: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
