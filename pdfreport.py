from reportlab.lib.pagesizes import letter
from datetime import datetime
import requests
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import LongTable

class FooterDocTemplate(SimpleDocTemplate):
    def __init__(self, filename, COMPANY_EMAIL, COMPANY_NAME, domain, **kwargs):
        self.COMPANY_EMAIL = COMPANY_EMAIL
        self.COMPANY_NAME = COMPANY_NAME
        self.domain = domain
        SimpleDocTemplate.__init__(self, filename, **kwargs)

    def handle_pageEnd(self):
        # Add footer on each page end
        self.canv.setFont("Helvetica", 10)
        self.canv.setFillColor(colors.blue)
        self.canv.drawCentredString(letter[0] / 2, 30, self.COMPANY_EMAIL)

        # Add date on top right corner
        self.canv.setFont("Helvetica", 10)
        self.canv.setFillColor(colors.black)
        self.canv.drawString(letter[0] - 100, letter[1] - 30, datetime.now().strftime('%Y-%m-%d'))

        # Add page number at bottom right
        self.canv.setFont("Helvetica", 10)
        self.canv.drawRightString(letter[0] - 30, 30, f"Page {self.canv.getPageNumber()}")

        # Add "Pentest Report: {domain}" on top left corner
        self.canv.setFont("Helvetica", 10)
        self.canv.drawString(30, letter[1] - 30, f"Pentest Report: {self.domain}")

        SimpleDocTemplate.handle_pageEnd(self)


class PDFReport:
    def __init__(self, filepath, COMPANY_NAME, COMPANY_EMAIL, COMPANY_LOGO_URL):
        self.filepath = filepath
        self.COMPANY_NAME = COMPANY_NAME
        self.COMPANY_EMAIL = COMPANY_EMAIL
        self.COMPANY_LOGO_URL = COMPANY_LOGO_URL
        self.logo_path = "logo.jpg"
        self.styles = getSampleStyleSheet()

    def download_logo(self):
        try:
            response = requests.get(self.COMPANY_LOGO_URL, timeout=5)
            if response.status_code == 200:
                with open(self.logo_path, 'wb') as f:
                    f.write(response.content)
                return True
        except requests.exceptions.RequestException as e:
            print(f"Couldn't download the logo due to an error: {e}")
        return False

    def create_paragraph(self, name, items):
        if not items:
            return Paragraph(f"No {name} found.", self.styles["ParagraphStyle"])
        else:
            output = f"{len(items)} {name} found:\n"
            for item in items:
                output += f"- {item}\n"
            return Paragraph(output, self.styles["ParagraphStyle"])

    def generate(self, url, leaks, subdomains, techs, protected_domains, non_protected_domains, wordpress_sites,
                 non_wordpress_sites, found_directories):
        # Calculate total subdomains and Cloudflare status
        total_subdomains = len(protected_domains) + len(non_protected_domains)
        non_protected_subdomains = len(non_protected_domains)

        # Initialize the story
        story = []

        try:
            self.styles.add(ParagraphStyle(name='ParagraphStyle', fontSize=10, textColor=colors.black))
        except KeyError:
            pass

        # Download the logo and add it to the story
        if self.download_logo():
            logo = Image(self.logo_path, width=200, height=200)
            story.append(logo)
        else:
            story.append(Paragraph("<font size=14>Placeholder logo</font>", self.styles["Normal"]))

        centered_style = ParagraphStyle(name='Centered', parent=self.styles['Normal'], alignment=TA_CENTER)

        story.append(Spacer(1, 12))

        # Add total subdomains found
        story.append(Paragraph(f"<font size=18>Total Subdomains Found: {total_subdomains}</font>", centered_style))
        story.append(Spacer(1, 12))

        # Add Cloudflare status
        story.append(
            Paragraph(f"<font size=18>Sites Not Using Cloudflare: {non_protected_subdomains}/{total_subdomains}</font>",
                      centered_style))
        story.append(Spacer(1, 50))

        # Add company name
        story.append(Spacer(1, 12))
        story.append(Paragraph(f"<font size=11>Prepared by: {self.COMPANY_NAME}</font>", centered_style))

        # Add page break
        story.append(PageBreak())

        # Add Leaks Title
        story.append(Paragraph(f"<font size=14>Leaks</font>", centered_style))
        story.append(Spacer(1, 12))
        # Add leaks report
        leaks_report = generate_leaks_report(len(leaks), leaks)
        story.append(Paragraph(leaks_report, self.styles["ParagraphStyle"]))
        story.append(Spacer(1, 12))

        # Add Subdomains Title
        story.append(Spacer(1, 12))
        subdomains_table = self.create_table("Subdomains", subdomains)
        story.append(subdomains_table)

        # Add Technologies Title
        story.append(Spacer(1, 12))
        techs_table = self.create_table("Technologies", techs)
        story.append(techs_table)

        # Add Protected Domains Title
        story.append(Spacer(1, 12))
        protected_domains_table = self.create_table("Protected domains", protected_domains)
        story.append(protected_domains_table)

        # Add Non-Protected Domains Title
        story.append(Spacer(1, 12))
        non_protected_domains_table = self.create_table("Non-protected domains", non_protected_domains)
        story.append(non_protected_domains_table)

        # Add WordPress Sites Title
        story.append(Spacer(1, 12))
        wordpress_sites_table = self.create_table("WordPress sites", wordpress_sites)
        story.append(wordpress_sites_table)

        # Add Non-WordPress Sites Title
        story.append(Spacer(1, 12))
        non_wordpress_sites_table = self.create_table("Non-WordPress sites", non_wordpress_sites)
        story.append(non_wordpress_sites_table)

        # Add Directories Title
        story.append(Spacer(1, 12))
        directories_table = self.create_table("Found directories", found_directories)
        story.append(directories_table)

        # Save the PDF file
        doc = FooterDocTemplate(self.filepath, self.COMPANY_EMAIL, self.COMPANY_NAME, url, pagesize=letter)
        doc.build(story)

    def create_table(self, name, items):
        if not items:
            return Paragraph(f"No {name} found.", self.styles["ParagraphStyle"])
        else:
            # Calculate available table width: total width - margins - inter-column space
            table_width = letter[0] - 2 * inch - (1 * (2 - 1)) / inch
            col_widths = [table_width * 0.1, table_width * 0.9]  # Adjust as needed
        
            table_data = [['No.', name]]
            for i, item in enumerate(items, start=1):
                item_paragraph = Paragraph(item, self.styles["Normal"])  # Wrap the item in a Paragraph
                table_data.append([str(i), item_paragraph])  # Append the Paragraph to the table data
            table = LongTable(table_data, colWidths=col_widths, repeatRows=1)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            return table

def generate_cloudflare_report(num_unique_subdomains, num_using_cloudflare, cloudflare_status, non_protected_domains):
    # Format the list of non_protected_domains for the report
    non_protected_domains_str = "<br/>".join(f"• {domain}" for domain in non_protected_domains)

    # Modify the text to include the list of non_protected_domains if any exist
    text = f"""
    During the preliminary stage of our penetration test, a thorough initial scan was performed, which identified a total of {num_unique_subdomains} unique response subdomains.
    
    Further examination of these subdomains revealed a noteworthy statistic: {num_using_cloudflare} of them were found to be utilizing Cloudflare as a means of security and performance enhancement. {cloudflare_status}
    """
    if num_using_cloudflare > 0:
        text += f"\n<br/>The following subdomains were found not to be utilizing Cloudflare:<br/>{non_protected_domains_str}<br/>\n"

    text += """
    This is a significant observation that warrants further discussion, due to the possible exposure or leakage of information related to the servers hosting your website. Cloudflare, as a leading provider of content delivery network services, DDoS mitigation, Internet security, and distributed domain-name-server services, offers robust protection for many websites.
    
    However, the reliance on this tool also introduces certain considerations. The most salient concern is that of Distributed Denial of Service (DDoS) attacks, a common threat in the digital landscape.
    
    DDoS attacks involve overwhelming a network with traffic, which, if successful, can lead to extended periods of downtime. This can cause significant disruption to your visitors, impairing their ability to access your website and potentially compromising their experience.
    
    Moreover, it's vital to consider that the identified subdomains could be hosting additional sensitive data or critical functionalities. If these areas were to be compromised due to vulnerabilities, it might not only lead to data breaches but also to malfunctions in essential website operations. Such breaches could lead to a slew of issues ranging from regulatory penalties to reputational damage.
    
    In the end, while Cloudflare offers substantial security benefits, it is crucial that we remain vigilant to the potential risks and vulnerabilities associated with its use. The purpose of this penetration test is not only to uncover potential vulnerabilities but also to provide you with a deeper understanding of your digital security landscape so you can better protect your operations in the future.
    """
    return text

def generate_wordpress_report(num_wordpress_sites, num_non_wordpress_sites, wordpress_sites):
    # Format the list of wordpress_sites for the report
    wordpress_sites_str = "<br/>".join(f"• {site}" for site in wordpress_sites)

    # Modify the text to include the list of wordpress_sites if any exist
    text = f"""
    During the course of our scan, we have identified a total of {num_wordpress_sites} sites that are currently utilizing WordPress as their content management system (CMS).
    
    Out of the total websites, {num_non_wordpress_sites} were found not to be using WordPress.
    """
    if num_wordpress_sites > 0:
        text += f"\n<br/>The following websites were found to be utilizing WordPress:<br/>{wordpress_sites_str}<br/>\n"

    text += """
    This observation is significant due to the security implications associated with the use of WordPress. While WordPress is known for its user-friendly interface and ease of use, it also is known to have security vulnerabilities that can be exploited by malicious actors.
    
    These vulnerabilities can lead to a variety of issues, including unauthorized access, data loss, and website defacement. Moreover, the widespread use of WordPress makes websites using this CMS attractive targets for automated attacks.
    
    As a part of our penetration testing service, we can help you identify potential vulnerabilities in your WordPress setup and provide recommendations to enhance your website security. These could include regular updates of WordPress core, themes, and plugins, and implementing robust security measures such as strong passwords and two-factor authentication.
    """
    return text

def generate_directory_report(num_directories_found, found_directories):
    # Format the list of found_directories for the report
    found_directories_str = "<br/>".join(f"• {directory}" for directory in found_directories)

    text = f"""
    The scan identified a total of {num_directories_found} common directories or files that were found on the websites.
    """
    if num_directories_found > 0:
        text += f"\n<br/>The following directories or files were found:<br/>{found_directories_str}<br/>\n"

    text += """
    This finding is crucial as it may signify potential security issues. Misconfigured file permissions or unsecured directories can lead to unauthorized access and data breaches. Sensitive information such as database credentials or confidential user data might be exposed if these directories are not properly secured.
    
    Additionally, access to certain directories might provide an attacker with valuable information about the system and help them craft more effective attacks. For example, access to the .htaccess file in an Apache server could reveal sensitive configuration data.
    
    It's recommended to ensure all directories and files are secured with appropriate permissions, and any unnecessary or outdated files are removed from the server. Regular audits of your file and directory structure can help detect any potential issues early on.
    """
    return text

def generate_leaks_report(num_leaks, leaks):
    # Check if leaks is an error message
    if isinstance(leaks, dict) and 'error' in leaks:
        return f"Database lookup error: {leaks['message']}"
        
    # Otherwise proceed as before
    leaks_str = "<br/>".join(f"• {leak}" for leak in leaks)
    text = ""
    if num_leaks == 0:
        text = """
        Congratulations! Our scan didn't find any leaks associated with the domain. This is a good indication of well-implemented security practices. However, it's essential to remain vigilant. Individual employees must ensure they are not using their personal passwords within the company. A continuous effort should be made to educate all staff members about the potential risks and how to mitigate them.
        """
    else:
        text = f"""
        Our scan identified {num_leaks} leaks associated with the domain. Here are the leaks we found:<br/>{leaks_str}<br/>
        
        The presence of these leaks suggests a potential security risk. Personal or company emails appearing in public data leaks might be a result of third-party breaches. It's crucial to address these issues as soon as possible to prevent misuse of the information. 

        The risks involved can vary, ranging from phishing attempts and spam to more serious threats like credential stuffing attacks. For each leak, it's recommended to check the context and the data involved to assess its impact properly.

        Additionally, it's important to implement robust password policies within your organization. Employees should be encouraged to use unique passwords and regularly change them. Using a password manager can help manage this process more effectively. Moreover, consider implementing two-factor authentication as an additional layer of security.
        """
    return text