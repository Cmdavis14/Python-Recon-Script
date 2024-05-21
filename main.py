#!/usr/bin/env python3

from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

"""
Gathers informaiton about a website
Args:
    name (str): The name of the website.
    url (str): The URL of the website to be scanned.
    nmap_options (str): The options for the Nmap scan.
"""
def gather_info(name, url, nmap_options):
    domain_name = get_domain_name(url)
    ip_address= get_ip_address(domain_name) #changed from url
    nmap = get_nmap('-sV', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, robots_txt, nmap, whois)

"""
Creates a report with gathered information.
Args:
    name (str): The name of the website.
    full_url (str); The full URL of the website.
    domain_name (str): The domain name of the website.
    robots_txt (str): The contents of the robots.txt file.
    nmap (str): The results of the Nmap scan.
    whois (str): The WHOIS informaiton of the domain.
"""
def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name 
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)
                   

# Prompting User For Input:
name = input("Enter Name of Website: ")
url = input("Enter the Full URL to Scan: ")
nmap_options = input("Specify Nmap Scan Needed (e.g., sV for service version detection): ")


# Conver User Input to Nmap Option Format:
nmap_options = "-" + nmap_options


# Gathering Info and Creating Report
gather_info(name, url, nmap_options)

