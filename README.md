# httpx-and-http-probe-alternative
Here's a Python script that reads a list of URLs or subdomains from a text file, makes HTTP requests to each of them, and prints the status code of the response. It also has an option to check for a specific status code and give a response accordingly


# To use the script, follow these steps:

Create a text file called urls.txt in the same directory as the script.

Add a list of URLs or subdomains to the urls.txt file, with one URL or subdomain per line.

Run the script: python status_code_check.py

The script will read the list of URLs or subdomains from the urls.txt file and make an HTTP request to each one. 
It will then print the status code of the response. If you entered a specific status code to check for, the script will also print whether or not the status code of the response matches the one you specified.
