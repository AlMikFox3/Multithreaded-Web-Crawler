from urllib.parse import urlparse

def get_domain_name(url):
	try:
		sub_domain = get_sub_domain(url).split('.')
		results = sub_domain[-2] + '.' + sub_domain[-1]
	except:
		return ''
	return results

def get_sub_domain(url):
	try:
		return urlparse(url).netloc
	except:
		return ''


#print(get_domain_name('https://www.mail.google.com/drive'))