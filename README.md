# URL Health Checker

A high-performance Python script for bulk URL status checking using parallel processing.

## Features
- Multi-threaded URL checking with `ThreadPoolExecutor`
- Configurable timeout settings
- Automatic redirect following
- Type hints for better code clarity
- Error reporting for:
  - Non-200 status codes
  - Connection errors
  - Timeouts
- Clean console output of problematic URLs

## Requirements
- Python 3.8+ (for walrus operator)
- requests library

## Installation

```bash
. venv/bin/activate
python main.py
```

## Configuration
Modify these top-level variables in `main.py`:
- `TIMEOUT`: Set request timeout in seconds (default: 5)
- `urls`: Update the list of URLs to check
- `allow_redirects`: Change in check_url parameters if needed (default: True)

## Usage
1. Edit the `urls` list in `main.py`
2. Run the script:

## Performance Notes
- Uses concurrent.futures.ThreadPoolExecutor for parallel requests
- Processes all URLs in parallel by default
- Memory efficient - only stores problematic URLs
- Add `max_workers` parameter to ThreadPoolExecutor to limit concurrency

## License
MIT License - See [LICENSE](LICENSE) for details
