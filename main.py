import whois

domain = 'twitter.com'
# domain = input('Enter a domain name: ')

w = whois.whois(domain)

print(w)

# print(f"Registered by {w['org']}.\n", f"Expires on: {w['expiration_date'][0]}")