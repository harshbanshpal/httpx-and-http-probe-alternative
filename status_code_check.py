import requests

# Read the URLs or subdomains from the file
with open("urls.txt", "r") as file:
    lines = file.readlines()

# Prompt the user for a status code to check for
status_code = input("Enter a status code to check for (leave blank to skip): ")

# Make an HTTP request to each URL or subdomain
for line in lines:
    url = line.strip()
    try:
        response = requests.get(url)
        if status_code:
            if response.status_code == int(status_code):
                print(f"{url}: {response.status_code} (matches {status_code})")
            else:
                print(f"{url}: {response.status_code} (does not match {status_code})")
        else:
            print(f"{url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{url}: Error - {e}")
