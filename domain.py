from urllib.parse import urlparse


#Get domain name
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return 'in'


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return 'in sub'


#print(get_domain_name(r'https://thenewboston.com/'))