import requests

r = requests.get("https://www.ap.be/")
with open("homepage.html","w", encoding="utf-8") as file:
    file.write(r.text)
    