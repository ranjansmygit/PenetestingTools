import json
import requests
from typing import Dict

# JIRA credentials
jira_url = "https://jira.example.com"
jira_username = "your_username"
jira_password = "your_password"

# Microsoft Defender scan output
scan_output = json.load(open("scan_output.json"))

def create_jira_issue(issue_data: Dict):
    """
    Creates a JIRA issue using the provided issue data
    """
    headers = {
        "Content-Type": "application/json"
    }
    auth = (jira_username, jira_password)
    url = f"{jira_url}/rest/api/2/issue"
    response = requests.post(url, json=issue_data, headers=headers, auth=auth)
    if response.status_code != 201:
        raise ValueError(f"Failed to create JIRA issue: {response.text}")
    return response.json()

def create_jira_issues_from_scan_output(scan_output: Dict):
    """
    Creates JIRA issues for each vulnerability found in the scan output
    """
    for vulnerability in scan_output["vulnerabilities"]:
        issue_data = {
            "fields": {
                "project": {"key": "DEF"},
                "summary": vulnerability["title"],
                "description": vulnerability["description"],
                "issuetype": {"name": "Vulnerability"},
                "priority": {"name": "High"},
                "labels": [vulnerability["severity"]],
                "customfield_12345": {"value": vulnerability["cvss"]}
            }
        }
        create_jira_issue(issue_data)

create_jira_issue(issue_data: Dict)
create_jira_issues_from_scan_output(scan_output: Dict)
