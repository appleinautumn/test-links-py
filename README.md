# URL Status Checker

A Python script that checks the status of URLs in parallel using ThreadPoolExecutor. It reports any URLs that are not returning a successful (200) status code.

## Features

- Parallel URL checking for improved performance
- Configurable timeout settings
- URLs stored in a separate configuration file
- Skips empty lines and comments in the URL file
- Reports only problematic URLs

## Setup

1. Clone the repository:

```bash
git clone git@github.com:appleinautumn/test-links-py.git
cd test-links-py
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create your URLs file:

```bash
cp urls.txt.example urls.txt
```

5. Add your URLs to `urls.txt`, one URL per line. Lines starting with '#' are treated as comments and will be ignored.

6. Run the app

```bash
python main.py
```

## Requirements
- Python 3.8+ (for walrus operator)
- requests library

## Configuration

### URLs File
- The URLs to check should be stored in `urls.txt`
- Each URL should be on a new line
- Lines starting with '#' are treated as comments
- Empty lines are ignored
- `urls.txt` is git-ignored, so you can maintain different URL lists in different environments
- Use `urls.txt.example` as a template

### Timeout Setting
- The default timeout for URL checks is 5 seconds
- You can modify the `TIMEOUT` constant in `main.py` to adjust this

## Performance Notes
- Uses concurrent.futures.ThreadPoolExecutor for parallel requests
- Processes all URLs in parallel by default
- Memory efficient - only stores problematic URLs
- Add `max_workers` parameter to ThreadPoolExecutor to limit concurrency

## License
MIT License - free for personal and commercial use
