import os
import subprocess



"""
Runs an Nmap scan with the specified options on the given IP address.
Args:
    options (str): The options to be passed to the Nmap command.
    ip (str): The IP address to be scanned.
Returns:
    str: The output of the Nmap scan. 
"""
def get_nmap(options, ip):
    command = ["nmap", options, ip]
    try:
        results = subprocess.check_output(command, universal_newlines=True)
        return results
    except subprocess.CalledProcessError as e:
        return f"Error executing namp: {e.output}"
