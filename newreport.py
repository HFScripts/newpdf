import os
import re
import requests
import subprocess
from datetime import datetime
from urllib.parse import urlparse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from utils.pdfreport import PDFReport
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = '12341453125315'
COMPANY_LOGO_URL = 'https://i.ibb.co/MZsXm4J/websecl-image.png'
COMPANY_EMAIL = 'admin@robotsecurity.com'
COMPANY_NAME = 'Robot Security'

def count_results(leak_lookup_api_key, query):
    url = 'https://leak-lookup.com/api/search'
    data = {'key': leak_lookup_api_key, 'type': 'domain', 'query': query}
    try:
        response = requests.post(url, data=data)
        return response.json()
    except Exception as e:
        print(f'Error occurred: {e}')
        return None

def subdomain_enumeration(domain):
    # add your commands for subdomain enumeration
    commands = [
        f'dmitry -winse {domain}',
        f'theHarvester -d {domain} -b baidu,bevigil,bing,bingapi,certspotter,crtsh,dnsdumpster,duckduckgo,hackertarget,otx,threatminer,urlscan,yahoo',
        f'assetfinder --subs-only {domain}',
        f'getallurls -subs {domain}',
        f'subfinder -silent -t 10 -timeout 3 -nW -d {domain}',
    ]
    subdomains = []
    for command in commands:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for line in lines:
                if re.match("^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", line):
                    line = line.replace('www.', '')  # remove www. from the subdomain
                    subdomains.append(line)
        except Exception as e:
            print(f'Error occurred: {e}')
    
    # remove duplicates and add the root domain
    subdomains = list(set(subdomains))
    subdomains.append(domain)
    return subdomains

def technology_analysis(subdomains, root_domain):
    techs = []
    for subdomain in subdomains:
        try:
            subdomain = subdomain.replace("http://", "").replace("https://", "")  # Remove "http://" or "https://"
            for protocol in ["http://", "https://"]:
                full_subdomain = protocol + subdomain
                result = subprocess.run(f'whatweb {full_subdomain}', shell=True, capture_output=True, text=True)
                lines = result.stdout.split('\n')
                for line in lines:
                    line = re.sub(r'\x1b\[.*?m', '', line)  # Remove escape sequences
                    if line.startswith('http://') or line.startswith('https://'):  # Only keep lines that start with http(s)
                        domain = line.split()[0]  # Extract domain
                        if domain.endswith(root_domain):  # Check if the domain is a subdomain of root_domain
                            techs.append(line)
        except Exception as e:
            print(f'Error occurred: {e}')
    return techs

def cloudflare_check(techs):
    protected_domains = []
    non_protected_domains = []
    for tech in techs:
        # extract the domain from the start of the string until the first space
        domain = tech.split(' ')[0]
        if 'cloudflare' in tech.lower():  # make case insensitive
            protected_domains.append(domain)
        else:
            non_protected_domains.append(domain)
    return protected_domains, non_protected_domains

def port_scanning(non_protected_domains):
    scanned_ports = []
    for url in non_protected_domains:
        domain = urlparse(url).netloc
        print(f'Scanning ports for {domain}...')
        try:
            result = subprocess.run(f'rustscan -g -b 2000 -a {domain}', shell=True, capture_output=True, text=True)
            scanned_ports.append(result.stdout)
        except Exception as e:
            print(f'Error occurred: {e}')
    return scanned_ports

def wordpress_check(all_domains):
    wordpress_sites = []
    non_wordpress_sites = []

    for domain in all_domains:
        print(f'Checking if {domain} is running WordPress...')
        try:
            result = subprocess.run(f'wpscan --no-update --url {domain}', shell=True, capture_output=True, text=True)
            if "Scan Aborted: The remote website is up, but does not seem to be running WordPress." in result.stdout:
                non_wordpress_sites.append(domain)
            elif "Scan Aborted" not in result.stdout:
                wordpress_sites.append(domain)
        except Exception as e:
            print(f'Error occurred: {e}')

    return wordpress_sites, non_wordpress_sites

def common_files_check(all_domains):
    directories_to_check = [ 
        '.htaccess',
        '.git/HEAD',
        '.env',
        'phpinfo.php',
        'robots.txt',
        'sitemap.xml',
        'crossdomain.xml',
        'downloads',
        'backups',
    ]
    
    found_directories = []

    for domain in all_domains:
        for directory in directories_to_check:
            url = domain + '/' + directory
            try:
                response = requests.get(url, verify=False)
                if response.status_code == 200:
                    found_directories.append(url)
            except requests.exceptions.SSLError as e:
                # Try the other protocol if an SSLError occurs
                if 'https://' in url:
                    url = 'http://' + url.split('https://')[1]
                else:
                    url = 'https://' + url.split('http://')[1]
                try:
                    response = requests.get(url, verify=False)
                    if response.status_code == 200:
                        found_directories.append(url)
                except Exception as e:
                    pass
            except Exception as e:
                pass
    
    return found_directories

def main():
    domain = input('Enter the domain to be tested: ')
    print('Checking for leaks...')
    leaks = count_results(API_KEY, domain)
    print(f'Leaks found: {leaks}')
    print('Enumerating subdomains...')
    subdomains = subdomain_enumeration(domain)
    subdomains = list(set(subdomains))
    print(f'Subdomains found: {subdomains}')
    print('Performing technology analysis...')
    techs = technology_analysis(subdomains, domain)
    print(f'Technologies found: {techs}')
    protected_domains, non_protected_domains = cloudflare_check(techs)
    print(f'Protected domains: {protected_domains}')
    print(f'Non-protected domains: {non_protected_domains}')
    scanned_ports = port_scanning(non_protected_domains)
    print(f'Port scan results: {scanned_ports}')
    all_domains = protected_domains + non_protected_domains
    wordpress_sites, non_wordpress_sites = wordpress_check(all_domains)
    print(f'WordPress sites: {wordpress_sites}')
    print(f'Non-WordPress sites: {non_wordpress_sites}')
    found_directories = common_files_check(all_domains)
    print(f'Common files/directories found: {found_directories}')
    report = PDFReport("report.pdf", COMPANY_NAME, COMPANY_EMAIL, COMPANY_LOGO_URL)
    report.generate(domain, leaks, subdomains, techs, protected_domains, non_protected_domains, wordpress_sites, non_wordpress_sites, found_directories, scanned_ports)

    # Delete the logo file
    if os.path.exists("logo.jpg"):
        os.remove("logo.jpg")

if __name__ == '__main__':
    main()
