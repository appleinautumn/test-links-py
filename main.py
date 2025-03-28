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
def check_url(url: str, timeout: float = TIMEOUT) -> Tuple[str, str]:
    try:
        response = requests.head(url, allow_redirects=True, timeout=timeout)
        if response.status_code == 200:
            return url, "OK"
        return url, f"Error {response.status_code}"
    except requests.RequestException as e:
        return url, f"Error: {e}"

def main():
    urls = load_urls()
    if not urls:
        return

    # Check URLs using ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(check_url, urls))

    # Print status for all URLs
    failed_urls = []
    for url, status in results:
        print(f"{url} -> {status}")
        if status != "OK":
            failed_urls.append((url, status))

    # Print summary of failed URLs
    if failed_urls:
        print("\nSummary of failed URLs:")
        print("-" * 40)
        for url, status in failed_urls:
            print(f"{url}")
    else:
        print("\nAll URLs are working correctly!")

if __name__ == "__main__":
    main()
