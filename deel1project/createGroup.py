import requests
import getpass


def main():
    # token = getpass.getpass("geef je private token in: ")
    gitlabUrl = "https://gitlab.apstudent.be/api/v4/groups"
    token = "glpat-uR14qd11RVpNG-NsNnGb"    # voor testing


    headers = {
    "Authorization": f"Bearer {token}"
    }

    groupname = "studenten"

    groupdata = {
    "name": groupname,
    "path": groupname.lower(),
    "visibility": "private",
    }

    response = requests.post(gitlabUrl, headers=headers,json=groupdata)
    print(response.status_code)


if __name__ == "__main__":
    main()