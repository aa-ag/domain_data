import whois

domain = 'twitter.com'
# domain = input('Enter a domain name: ')

w = whois.whois(domain)

# print(w)

print(f"\nRegistered by {w['org']}.\n", f"Expires on: {w['expiration_date']}")