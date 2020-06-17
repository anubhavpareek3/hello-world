def email_list(domains):
	emails = []
	for dnames,users in domains.items():
	  for user in users:
	    emails.append(user +"@" + dnames)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
