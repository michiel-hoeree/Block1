import requests
import sys


r = requests.get("https://www.ap.be/")
with open(sys.argv[1],"w", encoding="utf-8") as file:
    file.write(r.text)