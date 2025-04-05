# Crossref MCP Server

🔍 Enable AI assistants to search and access academic paper metadata through Crossref using a simple MCP interface.

The Crossref MCP Server provides a bridge between AI assistants and Crossref's database of academic literature through the Model Context Protocol (MCP). It allows AI models to search for scientific articles by DOI, title, or keywords, access their metadata, and retrieve journal and funder information in a programmatic way.

## ✨ Core Features

- 🔎 Work Search by Query: Find papers using keywords, titles, or authors ✅
- 📊 Metadata Access: Retrieve detailed metadata for specific papers by DOI ✅
- 📚 Journal Search: Find journals in the Crossref database ✅
- 💰 Funder Search: Discover funding organizations and their supported research ✅

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- FastMCP library

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/JackKuo666/Crossref-MCP-Server.git
   cd Crossref-MCP-Server
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## 📊 Usage

Start the MCP server:

```bash
python crossref_server.py
```

## Usage with Claude Desktop or Cline

Add this configuration to your `cline_mcp_settings.json` or `claude_desktop_config.json`:

(Mac OS)

```json
{
  "mcpServers": {
    "crossref": {
      "command": "python",
      "args": ["-m", "crossref_server.py"]
      }
  }
}
```

(Windows version):

```json
{
  "mcpServers": {
    "crossref": {
      "command": "C:\\Users\\YOUR\\PATH\\miniconda3\\envs\\mcp_server\\python.exe",
      "args": [
        "D:\\code\\YOUR\\PATH\\Crossref-MCP-Server\\crossref_server.py"
      ],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 🛠 MCP Tools

The Crossref MCP Server provides the following tools:

1. `search_works_by_query`: Search for scholarly works using keywords, titles, or authors.
2. `get_work_metadata`: Get detailed metadata for a specific work using its DOI.
3. `search_journals`: Search for journals in the Crossref database.
4. `search_funders`: Search for funding organizations in the Crossref database.

### Searching Works by Query

You can ask the AI assistant to search for papers using keywords:
```
Can you search Crossref for papers about "machine learning in healthcare"?
```

### Getting Work Metadata by DOI

You can get detailed metadata for a specific paper using its DOI:
```
Can you show me the metadata for the paper with DOI 10.1038/nature14539?
```

### Searching Journals

You can search for journals in the Crossref database:
```
Can you find journals related to "artificial intelligence" in Crossref?
```

### Searching Funders

You can search for funding organizations:
```
Can you find information about the "National Science Foundation" in Crossref?
```


## 📁 Project Structure

- `crossref_server.py`: The main MCP server implementation using FastMCP
- `crossref_search.py`: Contains the logic for searching Crossref and retrieving metadata

## 🔧 Dependencies

- Python 3.10+
- FastMCP (mcp)
- requests
- bs4
- habanero

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Note

This tool uses the Crossref API to access publicly available metadata about academic works. For better API access priority, it's recommended to provide your email address when initializing the CrossrefSearch class.
