from requests import get, post, delete, options, head

s = "get"

response = eval(s)("https://google.com")


print(response.status_code)