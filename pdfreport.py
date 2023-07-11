from reportlab.lib.pagesizes import letter
from datetime import datetime
import requests
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet

class FooterDocTemplate(SimpleDocTemplate):
    def __init__(self, filename, COMPANY_EMAIL, COMPANY_NAME, **kwargs):
        self.COMPANY_EMAIL = COMPANY_EMAIL
        self.COMPANY_NAME = COMPANY_NAME
        SimpleDocTemplate.__init__(self, filename, **kwargs)

    def handle_pageEnd(self):
        # Add footer on each page end
        self.canv.setFont("Helvetica", 10)
        self.canv.drawCentredString(letter[0] / 2, 30, self.COMPANY_EMAIL)

        # Add date on top right corner
        self.canv.setFont("Helvetica", 10)
        self.canv.drawString(letter[0] - 100, letter[1] - 30, datetime.now().strftime('%Y-%m-%d'))

        # Add "Pentest Report: {COMPANY_NAME}" on top left corner
        self.canv.setFont("Helvetica", 10)
        self.canv.drawString(30, letter[1] - 30, f"Pentest Report: {self.COMPANY_NAME}")
        
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
        response = requests.get(self.COMPANY_LOGO_URL)
        if response.status_code == 200:
            with open(self.logo_path, 'wb') as f:
                f.write(response.content)
            return True
        return False

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

        # Add company name
        story.append(Spacer(1, 12))
        story.append(Paragraph(f"<font size=22>Prepared by: {self.COMPANY_NAME}</font>", centered_style))

        story.append(Spacer(1, 12))
    
        # Add total subdomains found
        story.append(Paragraph(f"<font size=18>Total Subdomains Found: {total_subdomains}</font>", centered_style))
        story.append(Spacer(1, 12))
    
        # Add Cloudflare status
        story.append(Paragraph(f"<font size=18>Sites Not Using Cloudflare: {non_protected_subdomains}/{total_subdomains}</font>", centered_style))
        story.append(Spacer(1, 12))

        # Add page break
        story.append(PageBreak())
    
        if leaks.get('error', 'false') == 'true':
            story.append(Paragraph("We were unable at this point in time to determine if any of your companies emails are in breaches.", self.styles["ParagraphStyle"]))
        else:
            story.append(Paragraph("Leaks found: " + str(leaks), self.styles["ParagraphStyle"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph("Subdomains found: " + str(subdomains), self.styles["ParagraphStyle"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph("Technologies found: " + str(techs), self.styles["ParagraphStyle"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph("Protected domains: " + str(protected_domains), self.styles["ParagraphStyle"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph("Non-protected domains: " + str(non_protected_domains), self.styles["ParagraphStyle"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph("WordPress sites: " + str(wordpress_sites), self.styles["ParagraphStyle"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph("Non-WordPress sites: " + str(non_wordpress_sites), self.styles["ParagraphStyle"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph("Common files/directories found: " + str(found_directories), self.styles["ParagraphStyle"]))
    
        # Save the PDF file
        doc = FooterDocTemplate(self.filepath, self.COMPANY_EMAIL, self.COMPANY_NAME, pagesize=letter)
        doc.build(story)
