#!/usr/bin/env python3
import requests
import argparse
import os
import time

def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def fetch_urls(domain):
    page = 1
    all_urls = []

    print_color(f"\n[+] Fetching URLs for domain: {domain}", "96")  # Cyan
    while True:
        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/url_list?limit=100&page={page}"
        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.RequestException as e:
            print_color(f"[-] Request error for {domain} page {page}: {e}", "91")
            break

        if response.status_code != 200:
            print_color(f"[-] Failed to fetch page {page} for {domain} (Status: {response.status_code})", "91")
            break

        data = response.json()
        url_list = data.get("url_list", [])

        if not url_list:
            print_color(f"[!] No more URLs found on page {page} — stopping.", "93")  # Yellow
            break

        for item in url_list:
            extracted_url = item.get("url")
            if extracted_url:
                print(extracted_url)
                all_urls.append(extracted_url)

        print_color(f"[+] Page {page}: Found {len(url_list)} URLs", "92")  # Green
        page += 1
        time.sleep(1)  # Be nice to the API

    return all_urls

def main():
    parser = argparse.ArgumentParser(description="OTX AlienVault URL scraper.")
    parser.add_argument("-l", "--list", required=True, help="Input file with list of domains")
    parser.add_argument("-o", "--output", default="collected_urls.txt", help="Output file name (default: collected_urls.txt)")
    args = parser.parse_args()

    domains_file = args.list
    output_file = args.output

    if not os.path.isfile(domains_file):
        print_color(f"[-] File not found: {domains_file}", "91")
        exit(1)

    with open(domains_file, "r") as f:
        domains = [line.strip() for line in f if line.strip()]

    total = 0
    with open(output_file, "w") as outfile:
        for domain in domains:
            urls = fetch_urls(domain)
            for url in urls:
                outfile.write(url + "\n")
            total += len(urls)

    print_color(f"\n[0] Done. Total URLs collected: {total}", "92")
    print_color(f"[0] Saved to: {output_file}", "94")

if __name__ == "__main__":
    main()