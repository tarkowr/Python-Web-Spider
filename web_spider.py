import requests

links_file = open("links.txt", "r")
results_file = open("results.txt", "w")

# Configure cookie to send with HTTP req
jar = requests.cookies.RequestsCookieJar()
jar.set("replace-with-session-cookie-name", "replace-with-auth-session-id", domain="replace-with-domain", path="/")

query = ["replace-with-search-string"]
number_found = 0
context = 100  # 0 will write the entire http response to the passwords file.

for url in links_file.readlines():
	res = requests.get(url.strip(), cookies=jar)
	res_text = res.text.strip().lower()

	for word in query:
		index = res_text.find(word)

		if index != -1:
			number_found = number_found + 1
			results_file.write("\"%s\" found in %s \n" % (word.title(), url))

			text_to_write = res_text

			if context != 0:
				text_to_write = res_text[index-context:index+context]

			results_file.write(text_to_write + "\n\n")

print("Number of instances found: {}".format(number_found))

links_file.close()
results_file.close()