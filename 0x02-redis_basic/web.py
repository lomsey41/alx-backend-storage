#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
import time
from functools import lru_cache

# Define the slowwly base URL to simulate slow responses
SLOWWLY_BASE_URL = 'http://slowwly.robertomurray.co.uk/delay/{delay}/url/'

# Function to fetch a web page
def fetch_page(url):
    response = requests.get(url)
    return response.text

# Function to get the key for caching the access count
def get_count_key(url):
    return f"count:{url}"

# Function to track the number of times a URL is accessed
def track_access_count(url):
    count_key = get_count_key(url)
    count = int(redis.get(count_key) or 0) + 1
    redis.set(count_key, count, ex=10)

# Function to get the page content with caching and tracking
@lru_cache(maxsize=None)
def get_page(url):
    # Simulate slow response using slowwly service with 5 seconds delay
    slowwly_url = SLOWWLY_BASE_URL.format(delay=5) + url

    # Fetch the page and track the access count
    page_content = fetch_page(slowwly_url)
    track_access_count(url)

    return page_content

if __name__ == "__main__":
    # Test the get_page function
    for _ in range(5):
        url = "https://example.com"  # Replace with the desired URL to test
        page_content = get_page(url)
        print(f"URL: {url}\nContent: {page_content[:100]}...\n")

    # Wait for 15 seconds to test cache expiration
    time.sleep(15)

    # Access the same URL again to see if it triggers a new fetch
    page_content = get_page(url)
    print(f"URL: {url}\nContent: {page_content[:100]}...\n")
