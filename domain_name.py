import tldextract

"""
Extracts the domain name from a given URL.

Args:
    url (str): The URL from which the domain name is extracted
Returns:
    str: The extracted domain name.

"""

# Extracting Components of the URL Using tldextract
def get_domain_name(url):
    extracted = tldextract.extract(url)
    domain_name = f"{extracted.domain}.{extracted.suffix}"
    return domain_name
