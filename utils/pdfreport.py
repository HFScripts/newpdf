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
from utils.report_parts import create_paragraph, generate_confidentiality_statement, generate_omg_cables_rubber_ducky_report, generate_insider_threats_report, generate_wifi_hacking_mitm_report, generate_bib_report, generate_git_directory_exposure_report, generate_exif_data_exposure_report, generate_idor_report, generate_lfi_report, generate_rfi_report, generate_sqli_report, generate_xss_report, generate_pimeyes_report, generate_file_upload_bypass_report, generate_username_enumeration_report, generate_2fa_bypass_report, generate_account_takeover_report, generate_cloudflare_report, generate_wordpress_report, generate_directory_report, generate_leaks_report

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

    def generate_image_path(self, image_name):
        return f"./images/{image_name}"

    def create_image(self, path, width=420, height=250):
        return Image(path, width, height)

    def create_scanned_ports_table(self, name, items):
        if not items:
            # Add your custom statement here
            return Paragraph(f"Port scanning wasn't completed due to Cloudflare protecting the servers."
                             f" There are a number of ways we can probe into the site to see if we can obtain a leak,"
                             f" however as of this scan those tests are set as untested.", 
                             self.styles["ParagraphStyle"])
        else:
            # Calculate available table width: total width - margins - inter-column space
            table_width = letter[0] - 2 * inch - (1 * (2 - 1)) / inch
            col_widths = [table_width * 0.1, table_width * 0.9]  # Adjust as needed

            table_data = [['No.', name]]
            for i, item in enumerate(items, start=1):
                item_paragraph = Paragraph("<br/>".join(item.split("\n")), self.styles["Normal"])  # Wrap each line in a new Paragraph
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
    
    def generate(self, url, leaks, subdomains, techs, protected_domains, non_protected_domains, wordpress_sites,
                 non_wordpress_sites, found_directories, scanned_ports):
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
            Paragraph(f"<font size=18>Unique Subdomains Not Using Cloudflare: {non_protected_subdomains}/{total_subdomains}</font>",
                      centered_style))
        story.append(Spacer(1, 40))

        # Add company name
        story.append(Spacer(1, 12))
        story.append(Paragraph(f"<font size=11>Prepared by: {self.COMPANY_NAME}</font>", centered_style))

        # Always at the bottom of the code
        story.append(Spacer(1, 250))
        story.append(generate_confidentiality_statement(self))
        story.append(Spacer(1, 12))

        # Add page break
        story.append(PageBreak())

        # Add Leaks Title
        story.append(Paragraph(f"<font size=14>Leaks</font>", centered_style))
        story.append(Spacer(1, 12))
        # Add leaks report
        leaks_report = generate_leaks_report(leaks)
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
        protected_domains_table = self.create_table("Sites with Cloudflare", protected_domains)
        story.append(protected_domains_table)

        # Add Non-Protected Domains Title
        story.append(Spacer(1, 12))
        non_protected_domains_table = self.create_table("Sites without Cloudflare", non_protected_domains)
        story.append(non_protected_domains_table)

        # Add WordPress Sites Title
        story.append(Spacer(1, 12))
        wordpress_sites_table = self.create_table("WordPress sites", wordpress_sites)
        story.append(wordpress_sites_table)

        # Add Directories Title
        story.append(Spacer(1, 12))
        directories_table = self.create_table("Found directories", found_directories)
        story.append(directories_table)

        # Add Port Scanning Results Title
        story.append(Spacer(1, 12))
        scanned_ports_table = self.create_scanned_ports_table("Port Scanning Results", scanned_ports)
        story.append(scanned_ports_table)

        # Add your new sections with titles
        story.append(PageBreak())
        story.append(generate_omg_cables_rubber_ducky_report(self))
        ducky_image = self.create_image(self.generate_image_path("ducky.png"))
        story.append(ducky_image)
        story.append(Spacer(1, 12))
        
        story.append(PageBreak())
        story.append(Paragraph("<font size=14>Insider Threats</font>", self.styles["Title"]))
        story.append(generate_insider_threats_report(self))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph("<font size=14>Directory exposure</font>", self.styles["Title"]))
        story.append(generate_git_directory_exposure_report(self))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<font size=14>Exif in website images</font>", self.styles["Title"]))
        story.append(generate_exif_data_exposure_report(self))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<font size=14>Insecure direct object reference</font>", self.styles["Title"]))
        story.append(generate_idor_report(self))
        story.append(Spacer(1, 12))

        story.append(PageBreak())

        story.append(Paragraph("<font size=14>Parameter exploitation (index.php?id=)</font>", self.styles["Title"]))
        story.append(Paragraph("<font size=10>Local File Inclusion (LFI)</font>", self.styles["Title"]))
        story.append(Spacer(1, 12))
        story.append(generate_lfi_report(self, url))
        story.append(Paragraph("<font size=10>Remote File Inclusion (RFI)</font>", self.styles["Title"]))
        story.append(Spacer(1, 12))
        story.append(generate_rfi_report(self, url))
        story.append(Paragraph("<font size=10>MySQL Injection (SQLi)</font>", self.styles["Title"]))
        story.append(Spacer(1, 12))
        story.append(generate_sqli_report(self, url))
        story.append(Paragraph("<font size=10>Cross Site Scripting (XSS)</font>", self.styles["Title"]))
        story.append(Spacer(1, 12))
        story.append(generate_xss_report(self, url))

        story.append(PageBreak())
        story.append(Paragraph("<font size=14>Wi-Fi Hacking and MiTM Attacks</font>", self.styles["Title"]))
        story.append(generate_wifi_hacking_mitm_report(self))
        story.append(Spacer(1, 12))
        mitm_image = self.create_image(self.generate_image_path("mitm.png"))
        story.append(mitm_image)
        story.append(Spacer(1, 12))

        story.append(PageBreak())
        story.append(Paragraph("<font size=14>Browser in Browser Attacks</font>", self.styles["Title"]))
        story.append(generate_bib_report(self))
        story.append(Spacer(1, 12))
        bitb_image = self.create_image(self.generate_image_path("bitb.png"))
        story.append(bitb_image)
        story.append(Spacer(1, 12))

        story.append(PageBreak())
        story.append(Paragraph("<font size=14>File upload Bypass</font>", self.styles["Title"]))
        story.append(generate_file_upload_bypass_report(self, url))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<font size=14>Facial Recognition</font>", self.styles["Title"]))
        story.append(generate_pimeyes_report(self))

        story.append(Paragraph("<font size=14>Username Enumeration</font>", self.styles["Title"]))
        story.append(generate_username_enumeration_report(self, url))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<font size=14>2FA Bypassing</font>", self.styles["Title"]))
        story.append(generate_2fa_bypass_report(self, url))
        story.append(Spacer(1, 12))
        story.append(Spacer(1, 12))
        story.append(Paragraph("<font size=14>ATO (Account Takeover)</font>", self.styles["Title"]))
        story.append(generate_account_takeover_report(self, url))
        story.append(Spacer(1, 12))

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


