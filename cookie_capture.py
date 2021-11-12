from anonBrowser import*
#import anonBrowser

url = print('Enter the url: ')
ab = anonBrowser(proxies=[],\ user_agents=[('User-agent','My browser')])
for attempt in range(1, 10 ):
    ab.anonymize()
print '[*] Fetching page'
response = ab.open(url) for cookie in ab.cookie_jar:
        print cookieprint(headers)
