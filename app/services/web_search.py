from typing import Optional
from duckduckgo_search import DDGS as DDGS


# Example MCP Client placeholder (still optional)
class MCPClient:
    def __init__(self, config_path: str):
        # You can extend this later if you have a real MCP server
        pass

    def query(self, user_question: str) -> Optional[str]:
        """
        Query the MCP server with user_question.
        Right now returns None (mock).
        """
        return None


# Web Search Client using DuckDuckGo (no API key required)
class WebSearchClient:
    def __init__(self):
        self.ddg = DDGS()

    def search(self, user_question: str, max_results: int = 3) -> Optional[str]:
        """
        Perform a DuckDuckGo search.
        Returns a summarized response.
        """
        try:
            results = list(self.ddg.text(user_question, max_results=max_results))
            if not results:
                return None

            # Extract snippets
            snippets = [r.get("body") for r in results if r.get("body")]
            combined = "\n".join(snippets)

            return combined if combined else None
        except Exception as e:
            print(f"[ERROR] DuckDuckGo search failed: {e}")
            return None


# Initialize global clients
mcp_client = MCPClient(config_path="config/config.yaml")
web_search_client = WebSearchClient()


def web_search_pipeline(user_question: str) -> Optional[str]:
    """Pipeline: First query MCP, fallback to DuckDuckGo web search."""
    # Step 1: Try MCP (currently mock)
    mcp_response = mcp_client.query(user_question)
    if mcp_response:
        return mcp_response

    # Step 2: Fallback to DuckDuckGo
    web_response = web_search_client.search(user_question)
    if web_response:
        return web_response

    # Step 3: Nothing found
    return None
