import requests
from bs4 import BeautifulSoup
import re

#1. WAP to check if the given contact number is valid or invalid using regular expressions-


def validate_contact_number(contact_number):
    
    pattern = r'^\+?[1-9]\d{0,2}-?\d{3,}-?\d{3,}$'
    
    if re.match(pattern, contact_number):
        return True
    else:
        return False


contact_number = input("Enter a contact number: ")

if validate_contact_number(contact_number):
    print("The contact number is valid.")
else:
    print("The contact number is invalid.")


    #2. WAP to get the Social Links, Email & Contacts details of a website on user input.


def get_social_links(soup):
    social_links = []
    social_patterns = [r'facebook\.com', r'twitter\.com', r'linkedin\.com', r'instagram\.com']
    
    for a_tag in soup.find_all('a', href=True):
        for pattern in social_patterns:
            if re.search(pattern, a_tag['href']):
                social_links.append(a_tag['href'])
                break
                
    return social_links

def get_email(soup):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    email = None
    
    for paragraph in soup.find_all('p'):
        if re.search(email_pattern, paragraph.get_text()):
            email = re.search(email_pattern, paragraph.get_text()).group()
            break
            
    return email

def get_contacts(soup):
    contact_pattern = r'\+\d{1,3}\s\d{1,5}\s\d{4,10}'
    contact = None
    
    for paragraph in soup.find_all('p'):
        if re.search(contact_pattern, paragraph.get_text()):
            contact = re.search(contact_pattern, paragraph.get_text()).group()
            break
            
    return contact

def main():
    user_input = input("Enter the website URL: ")
    
    try:
        response = requests.get(user_input)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        social_links = get_social_links(soup)
        email = get_email(soup)
        contact = get_contacts(soup)
        
        print("Social links:")
        for link in social_links:
            print(link)
            
        if email:
            print("Email:", email)
        else:
            print("Email not found.")
            
        if contact:
            print("Contact:", contact)
        else:
            print("Contact not found.")
            
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
