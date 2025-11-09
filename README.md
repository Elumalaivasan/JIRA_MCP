# JIRA MCP Server

A Model Context Protocol (MCP) server that provides tools for interacting with JIRA issues. This server allows you to get issues assigned to users, fetch specific issue details, and update issue fields.

## Features

- Get issues assigned to a user by their NTID
- Get detailed information about specific JIRA issues
- Update issue fields (summary, status, assignee)

## Prerequisites

- Python 3.x
- Access to JIRA instance with appropriate permissions
- JIRA API token

## Installation

1. Install the required dependencies:

```bash
pip install fastmcp requests
```

2. Set up environment variables:

Create a `.env` file in the root directory with the following variables:
```
JIRA_URL=your_jira_instance_url
JIRA_TOKEN=your_jira_api_token
PORT=8000  # Optional, defaults to 8000
```

## Running the Server

1. Start the MCP server:

```bash
python main.py
```

The server will start on `http://127.0.0.1:8000` by default.

## Available Tools

### 1. Get Issues by NTID
- Tool: `get_issues`
- Description: Retrieves issues assigned to a user by their NTID
- Returns: List of issues with summary, status, assignee, and description

### 2. Get Issue Details
- Tool: `get_issue`
- Description: Gets detailed information about a specific issue by ID
- Returns: Issue details including summary, status, assignee, description, created date, and updated date

### 3. Update Issue
- Tool: `update_issue`
- Description: Updates fields of a specific issue
- Fields that can be updated: summary, status, assignee

## Docker Support

A Dockerfile is included for containerized deployment. To build and run using Docker:

```bash
# Build the Docker image
docker build -t jira-mcp-server .

# Run the container
docker run -p 8000:8000 --env-file .env jira-mcp-server
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|-----------|
| JIRA_URL | Your JIRA instance URL | Yes |
| JIRA_TOKEN | JIRA API token for authentication | Yes |
| PORT | Server port (default: 8000) | No |
