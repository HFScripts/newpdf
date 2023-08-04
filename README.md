# DocBot Security™ Penetration Testing Tool

Welcome to the DocBot Security™ Penetration Testing Tool. This utility is a white-label service designed to provide a comprehensive security overview and detailed report analysis for your website.

## Overview

Our tool performs various checks, scans, and analyses on your website, identifying potential security leaks, common files, scanned ports, and subdomains, among other things. It further evaluates technologies employed on the site and produces a PDF report for easy interpretation and actioning.

## Features

- Database leak identification
- Subdomain discovery
- Cloudflare usage analysis
- Technology scanning
- Wordpress site identification
- Common files and directory exposure analysis
- Port scanning
- Parameter discovery and testing
- Generation of comprehensive PDF reports

## How to Use
# First, install the necessary modules

python3 setup.py

# Specify the domain for the site you want to test
domain = "your-site.net"

# Specify your companies information
- comp_email="your-email@company.com"
- comp_name="Your Company Name"
- logo_url='https://your-logo-url.jpg'
- logo_backup='https://your-logo-backup-url.jpg'

# Run the penetration testing function with your parameters
python3 whitelabel-report.py

## Dependencies
Our tool uses a combination of Python scripts and modules to accomplish its tasks. The required dependencies are:\n
- Python 3.7+
- reportlab
- glob
- os
- fitz
- wpscan
- sublist3r
- gau (getallurls)
- whatweb
- subfinder
- theHarvester
- golang-go
- ruby-gems
- rustscan
- dmitry
- nmap

Please ensure these dependencies are installed and up-to-date.

## Warning

Please use this tool responsibly. Unauthorized penetration testing can be illegal and unethical. Always obtain proper permissions before conducting any penetration tests.

## Contributing

If you find any bugs, have any questions, or wish to contribute, feel free to create an issue or submit a pull request. We appreciate your help in improving our tool.\n


# TODO
Ideas for stuff to add:

- Identify WAF for each subdomain

- Crawl for API_keys in code

- Pipe each page into semgrep
wget https://www.target.com; semgrep scan index.html --config auto; rm index.html

- Text explaining the risk of shared domains and domain/ip history. Discuss how even when enabling cloudflare, somes sites may have tracked
the server IP as such you should move yoour server IP after protecting your site behind cloudflare.
Subdomains might also leak your servers IP so it's important to split them up or ensure they are properly protected.
As far as sharing the same server as other websites, in this case it can lead to one of the following possibilities:
1. Someone might register a domain with the same hosting company and be put on the same server as your site. In this instace the hacker can now try gain a shell on their own site and pivot to your files on that machine.
2. Another website on the same server might be vulnerable allowing for a similar pivot to occur.

- Keeping services and code updated if new vulnerabilities are found. Even for old software.

- Check to see if we can use the domain for emailing.

- Check for unused javascript files in the source code (on remote domains)

- Expand on port scan, check for other sites on ports, SSH versions etc.

- If wordpress is detected, it should be added to the document.

- Check for expired domains in source code for JS or remote elements that could be registered or exploited.


Refer to references
- https://purplesec.us/wp-content/uploads/2019/12/Sample-Penetration-Test-Report-PurpleSec.pdf
- https://whiteknightlabs.com/wp-content/uploads/2022/05/Sample-WKL-Network-Penetration-Test-Report.pdf
- https://underdefense.com/wp-content/uploads/2019/05/Anonymised-Infrastructure-Penetration-Testing-Report.pdf
