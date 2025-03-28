import requests
from concurrent.futures import ThreadPoolExecutor
from typing import Optional, Tuple
from pathlib import Path

# Add timeout parameter at the top
TIMEOUT = 5  # seconds

def load_urls(filepath: str = 'urls.txt') -> list[str]:
    """Load URLs from a text file, skipping empty lines and comments."""
    try:
        with open(filepath, 'r') as f:
            return [line.strip() for line in f
                   if line.strip() and not line.strip().startswith('#')]
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Please create it from {filepath}.example")
        return []

# Function to check if a URL is working
def check_url(url: str, timeout: float = TIMEOUT) -> Optional[Tuple[str, str]]:
    try:
        response = requests.head(url, allow_redirects=True, timeout=timeout)
        # Only return URLs that do not return a 200 status code
        if response.status_code != 200:
            return url, f"Error {response.status_code}"
    except requests.RequestException as e:
        return url, f"Error: {e}"

def main():
    urls = load_urls()
    if not urls:
        return

    # Check URLs using ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        results = [result for result in executor.map(check_url, urls) if result is not None]

    # Print only the problematic URLs
    for url, status in results:
        print(f"{url} -> {status}")

if __name__ == "__main__":
    main()
