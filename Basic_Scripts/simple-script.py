import requests
url = 'https://bbc.com' 
response= requests.get(url)
if response.status_code == 200:
    print("Sucessful!")
else:
    print("Failed")
print(response.text)
