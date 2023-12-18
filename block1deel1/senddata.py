import requests

voornaam = input("Voornaam: ")
achternaam = input("Achternaam: ")
data = {
    "voornaam": voornaam,
    "achternaam": achternaam
}

r = requests.post("https://httpbin.org/post",data=data)

print(f"De status code was {r.status_code}")
print(r.json())
