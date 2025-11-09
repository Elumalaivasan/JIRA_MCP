from fastmcp import FastMCP
import requests
import os
mcp = FastMCP(name="JIRA MCP Server")

jira_url = os.getenv("JIRA_URL")
token = os.getenv("JIRA_TOKEN")
@mcp.tool(description="Get issues assigned to a user by their NTID. Takes the NTID as input and returns a list of issues with details like summary, status, assignee, and description.")
def get_issues(NTID: str) -> dict:
    url = f"{jira_url}/rest/api/2/search"
    jql = (
        f"project = FFLPULSE AND assignee in ('{NTID}') "
        f"AND status in (Open, \"In Progress\", Reopened) ORDER BY created DESC"
    )
    payload = {
        "jql": jql,
        "startAt": 0,
        "maxResults": 15,
        "fields": ["summary", "status", "assignee","description"]
    }
    response = requests.post(url,json=payload, headers={"Authorization": f"Bearer {token}"})
    #response.raise_for_status()
    return response.json()

@mcp.tool(description="Get details of a specific issue by its ID. Takes the issue ID as input and returns details like summary, status, assignee, description, created date, and updated date.")
def get_issue(issue_id: str) -> dict:
    fields=["summary", "status", "assignee", "description", "created", "updated"]
    url = f"{jira_url}/rest/api/2/issue/{issue_id}?fields={','.join(fields)}"
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {token}"}
    )
    #response.raise_for_status()
    return response.json()

@mcp.tool(description="Update fields like summary, status,assignee of a specific issue by its ID")
def update_issue(issue_id: str, fields: dict) -> str:
    url = f"{jira_url}/rest/api/2/issue/{issue_id}"
    response = requests.put(
        url,
        json={"fields": fields},
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    return "Issue updated successfully" if response.status_code == 204 else f"Failed to update issue: {response.text}"



if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    mcp.run(transport="sse", host="127.0.0.1", port=port)