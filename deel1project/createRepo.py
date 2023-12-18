import requests
import getpass


def main():
    token = getpass.getpass("geef je private token in: ")
    gitlabUrl = "https://gitlab.apstudent.be/api/v4/projects"
    headers = {
    "Authorization": f"Bearer {token}"
    }
    repoName = "newRepo"
    username = "michiel.hoeree"
    project_data = {
    "name": repoName,
    "namespace": username,
    "visibility": "private",
    }

    response = requests.post(gitlabUrl, headers=headers,json=project_data)
    print(response.status_code)





if __name__ == "__main__":
    main()