import os
import subprocess


"""
Retrieves the WHOIS information for a given URL.
Prameter:
    url (str): The domain name to query WHOIS information for.
Results:
    str: The WHOIS information as a string.
"""
def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return results

