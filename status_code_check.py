import concurrent.futures
import requests

# Read the URLs or subdomains from the file
with open("urls.txt", "r") as file:
    lines = file.readlines()

# Prompt the user for a status code to check for
status_code = input("Enter a status code to check for (leave blank to skip): ")

# Define a function to make an HTTP request to a URL
def check_url(url):
    try:
        response = requests.get(url)
        if status_code:
            if response.status_code == int(status_code):
                print(f"{url}: \033[1;32m{response.status_code}\033[0m (matches {status_code})")
            else:
                print(f"{url}: \033[1;31m{response.status_code}\033[0m (does not match {status_code})")
        else:
            if 200 <= response.status_code < 300:
                print(f"{url}: \033[1;32m{response.status_code}\033[0m")
            elif 300 <= response.status_code < 400:
                print(f"{url}: \033[1;34m{response.status_code}\033[0m")
            elif 400 <= response.status_code < 500:
                print(f"{url}: \033[1;33m{response.status_code}\033[0m")
            else:
                print(f"{url}: \033[1;31m{response.status_code}\033[0m")
    except requests.exceptions.RequestException as e:
        print(f"{url}: Error - {e}")

# Use a thread pool to concurrently make HTTP requests
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Add "https://" to the URL if it doesn't have a scheme
    urls = ["https://" + line.strip() if not line.startswith("http://") and not line.startswith("https://") else line.strip() for line in lines]
    results = [executor.submit(check_url, url) for url in urls]
