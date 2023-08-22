### 
#  WAP to check if the given contact  is valid or invalid using regular
#  expressions
#  Examples of different formats of s found on websites:
#  ● 2124567890
#  ● (212)-456-7890
#  ● 212.456.7890
#  ● 212 456 7890
#  ● +12124567890
#  ● +12124567890
#  ● +1 212.456.7890
#  ● +212-456-7890
#  ● 1-212-456-7890
#  As we can see above these are all the same s written in a different format, but they all are
#  valid s. If you cannot prove all of them to be valid s, hoping to have at least 5 of
#  them correctly to pass this.
###

import re

def is_valid_contact_num(num):
   
    pattern = r'^(?:\+\d{1,2}\s?)?(?:\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    match = re.match(pattern, num)
    
    return match is not None

# Test cases
nums = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

for num in nums:
    if is_valid_contact_num(num):
        print(f"{num} is a valid contact num.")
    else:
        print(f"{num} is an invalid contact num.")

### WAP to get the Social Links, Email & Contacts details of a website on user input.

import re
import requests

def get_website_details(url):
    try:
        
        response = requests.get(url)
        html_content = response.text

        
        socials = r'(https?://(?:www\.)?(?:facebook\.com|linkedin\.com)/[^"\']+)'
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        contact_pattern = r'\+\d{1,3}\s?\d{1,4}\s?\d{1,4}\s?\d{1,10}'

        social_links = re.findall(socials, html_content)
        emails = re.findall(email_pattern, html_content)
        contacts = re.findall(contact_pattern, html_content)

        return social_links, emails, contacts

    except Exception as e:
        return None, None, None


website = input("Enter the website URL: ")


social_links, emails, contacts = get_website_details(website)

# Print the extracted details
print("Social links -")
for link in social_links:
    print(link)

print("\nEmail:")
for email in emails:
    print(email)

print("\nContact:")
for contact in contacts:
    print(contact)
