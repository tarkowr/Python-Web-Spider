import requests

links_file = open("links.txt", "r")
password_text_file = open("passwords.txt", "w")

jar = requests.cookies.RequestsCookieJar()
jar.set("PHPSESSID", "replace-with-auth-session-id", domain="192.168.0.2", path="/")

query = "password"
passwords_found = 0
context = 100  # 0 will write the entire http response to the passwords file.

for url in links_file.readlines():
	res = requests.get(url.strip(), cookies=jar)
	res_text = res.text.strip().lower()
	index = res_text.find(query)
	if index != -1:
		passwords_found = passwords_found + 1
		password_text_file.write("Password found in %s \n" % url)

		text_to_write = res_text

		if context != 0:
			text_to_write = res_text[index-context:index+context]

		password_text_file.write(text_to_write + "\n\n")

print("Number of password instances found: {}".format(passwords_found))

links_file.close()
password_text_file.close()
