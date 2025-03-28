import requests
from concurrent.futures import ThreadPoolExecutor
from typing import Optional, Tuple

# List of URLs to check
urls = [
    "https://linode.com/docs/applications/big-data/how-to-install-and-configure-a-redis-cluster-on-ubuntu-1604/",
    "https://redis.io/topics/cluster-tutorial",
    "https://get-reddie.com/blog/redis4-cluster-docker-compose/",
    "https://www.pushradar.com/blog/5-reasons-why-you-should-use-redis-as-your-web-apps-database",
    "https://redislabs.com/blog/redis-mysql-fast-economic-scaling/",
    "https://itnext.io/learn-to-cache-your-nodejs-application-with-redis-in-6-minutes-745a574a9739",
    "https://redis.com/ebook/part-1-getting-started/chapter-1-getting-to-know-redis/1-1-what-is-redis/"
]

# Add timeout parameter at the top
TIMEOUT = 5  # seconds

# Function to check if a URL is working
def check_url(url: str, timeout: float = TIMEOUT) -> Optional[Tuple[str, str]]:
    try:
        response = requests.head(url, allow_redirects=True, timeout=timeout)
        # Only return URLs that do not return a 200 status code
        if response.status_code != 200:
            return url, f"Error {response.status_code}"
    except requests.RequestException as e:
        return url, f"Error: {e}"

# After (single call per URL)
with ThreadPoolExecutor() as executor:
    results = [result for result in executor.map(check_url, urls) if result is not None]

# Print only the problematic URLs
for url, status in results:
    print(f"{url} -> {status}")
