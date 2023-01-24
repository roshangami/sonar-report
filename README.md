# Sonar Report

SonarQube is an open-source platform developed by SonarSource for continuous inspection of code quality to perform automatic reviews with static analysis of code to detect bugs and code smells on 29 programming languages.

Reporting isn't available in SonarQube Community edition.

### Usage

Command help section:
```
% python3 sonarqube.py --help
usage: sonarqube.py [-h] [--url URL] [--port PORT] [--username USERNAME] [--password PASSWORD]

optional arguments:
  -h, --help           show this help message and exit
  --url URL            URL of the SonarQube server e.g. http://10.0.0.1 or https://20.0.0.1
  --port PORT          SonarQube server port, default=9000
  --username USERNAME  Username of the SonarQube
  --password PASSWORD  Password of the user
```

Example:
```
% python3 sonarqube.py --url http://10.20.30.40 --username admin --password admin
File exported successfully: sonar.json
```

### Author

Roshan Gami
