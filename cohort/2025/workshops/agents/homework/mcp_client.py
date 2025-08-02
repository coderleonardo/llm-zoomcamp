import asyncio
from fastmcp import Client

async def main():
    print("Attempting to connect to FastMCP server via stdio...")
    try:
        # Connect via stdio to a local script
        async with Client("weather_server.py") as client:
            tools = await client.list_tools()
            print(f"Available tools: {tools}")

    except Exception as e:
        print(f"Error connecting via stdio: {e}")


if __name__ == "__main__":
    asyncio.run(main())