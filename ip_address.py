import os # Importing the os module for system operations
import socket # Importing the socket module for network communication

 

"""
Retrieves the IP address corresponding to a domain name.
Args:
    domain_nmae (str): The domain name for which to retrieve the IP address
Returns:
    str: The IP address of the domain, or None if an error.
"""

def get_ip_address(domain_name): #changed from url
    try: #attempts to resolve the domain name to an IP address
        ip_address = socket.gethostbyname(domain_name)
        return ip_address # returns the resolved IP address
    except socket.gaierror as e:
        print(f"Error resolving domain name: {e}")
        return None #returns None to indicate error
