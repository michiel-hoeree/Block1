# een speciale folder gemaakt voor alle repos zodat main folder proper blijft
from git import Repo

link = input("Welke repo wilt u clonen? ")
try:
    Repo.clone_from(link,"./repos")
except:
    print("Het is niet gelukt dit project te clonen.")
