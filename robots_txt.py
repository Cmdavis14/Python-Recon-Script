import urllib.request
import io

"""
Retrieves the contents of the robots.txt file for a give url.
Args:
    url (str): the URL of the website
Returns:
    str: The contents of the robots.txt file.
"""
def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data = None)
    data = io.TextIOWrapper(req, encoding = 'utf-8')
    return data.read()
