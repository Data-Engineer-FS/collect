# pip install python-whois
from urllib.parse import urlparse
import whois
def whois_pack(domain):
    try:
        get_who = whois.whois(domain)
        return get_who
        # return get_who.get('name_servers')
    except Exception as e:
        print(e)
        return ''

domain_name = 'google.com'
get = whois_pack(urlparse(domain_name).netloc)
print(get)
