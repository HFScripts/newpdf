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

\`\`\`python
# First, install the necessary modules\n
python3 setup.py
# Specify the domain for the site you want to test\n
domain = "your-site.net"\n
comp_email="your-email@company.com"\n
comp_name="Your Company Name"\n
logo_url='https://your-logo-url.jpg'\n
logo_backup='https://your-logo-backup-url.jpg'\n
API_KEY = 'your-api-key'\n
\n
# Run the penetration testing function with your parameters\n
leaked_database_entries, all_subdomains_identified, technology_scan_output, live_domains_from_technology_scan, cloudflare_enabled, cloudflare_disabled, wordpress_sites, non_wordpress_sites, common_files_found, parameters_found, parameter_filenames, scanned_ports = fake_functions_to_run(domain, API_KEY)\n
\n
# Generate the PDF report with your results\n
test_pdf_func(domain, comp_email, comp_name, logo_url, logo_backup, leaked_database_entries, all_subdomains_identified, technology_scan_output, live_domains_from_technology_scan, cloudflare_enabled, cloudflare_disabled, wordpress_sites, non_wordpress_sites, common_files_found, parameters_found, parameter_filenames, scanned_ports)\n
\n
# Delete the logo file and cleanup leftover output files\n
if os.path.exists("logo.jpg"):\n
    os.remove("logo.jpg")\n
png_files = glob.glob('output*')\n
for filename in png_files:\n
    os.remove(filename)\n
\`\`\`\n
\n
## Dependencies\n
\n
Our tool uses a combination of Python scripts and modules to accomplish its tasks. The required dependencies are:\n
\n
- Python 3.7+\n
- reportlab\n
- glob\n
- os\n
\n
Please ensure these dependencies are installed and up-to-date.\n
\n
## Warning\n
\n
Please use this tool responsibly. Unauthorized penetration testing can be illegal and unethical. Always obtain proper permissions before conducting any penetration tests.\n
\n
## Contributing\n
\n
If you find any bugs, have any questions, or wish to contribute, feel free to create an issue or submit a pull request. We appreciate your help in improving our tool.\n
\n
## License\n
\n
This project is licensed under the MIT License. For more information, please see the [LICENSE](LICENSE) file.
