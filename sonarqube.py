import requests
import json
import argparse


def cmd_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL of the SonarQube server e.g. http://10.0.0.1 or https://20.0.0.1")
    parser.add_argument("--port", help="SonarQube server port, default=9000")
    parser.add_argument("--username", help="Username of the SonarQube")
    parser.add_argument("--password", help="Password of the user")

    args = parser.parse_args()
    if not args.port:
        args.port = "9000"
    return args.url, args.port, args.username, args.password


def get_sonar_issues(url, port, username, password):
    data = requests.post(f"{url}:{port}/api/authentication/login?login={username}&password={password}")
    if data.status_code == 401:
        return "401 Unauthorized: Check credentials"
    csv = requests.get(f"{url}:{port}/api/issues/search", cookies=data.cookies)
    issues = json.loads(csv.content.decode('utf-8'))
    json_object = json.dumps(issues, indent=4)

    # Writing to sample.json
    with open("sonar.json", "w") as outfile:
        outfile.write(json_object)
    return "True"


if __name__ == "__main__":
    loc, prt, uname, passwd = cmd_options()
    status = get_sonar_issues(loc, prt, uname, passwd)
    if status == "True":
        print("File exported successfully: sonar.json")
    else:
        print(f"Error: Failed to export the findings. STATUS: {status}")
