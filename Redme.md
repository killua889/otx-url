# OTX AlienVault URL Scraper

This Python script allows you to fetch URLs associated with given domains from the **OTX (AlienVault Open Threat Exchange)** API and save the collected URLs to a file. It supports fetching URLs in a paginated manner, automatically going through each page of results until no more URLs are found.

## Features

- Fetch URLs associated with multiple domains from OTX API.
- Saves the collected URLs to a user-defined output file.

## Requirements

- Python 3.x
- **requests** library (can be installed via `pip install requests`)

## Usage

1. **Clone the repository:**

```bash
git clone https://github.com/killua889/otx-url.git
cd otx-url
chmod +x otx-url.py
```
## Example :

```bash
python3 otx_url.py -l domains.txt -o output_urls.txt
```

`-l` Input file with a list of domains (one domain per line).

`-o` Output file where the collected URLs will be saved (default: collected_urls.txt).

Example domain.txt
```bash
example.com
example3.com
s.example.com
```