---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/tools/llama-index-tools-measurespace/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/tools/llama-index-tools-measurespace/README.md
---
# Measure Space Weather, Climate, Air Quality and Geocoding Tool

```bash
pip install llama-index-tools-measurespace
```

This tool connects to the MeasureSpace's API, using the measure-space-api Python package. You must initialize the tool with corresponding API keys from MeasureSpace and OpenAI (if you use OpenAI).

The tool has access to the following functions:

- hourly weather forecast (next 5 days)
- daily weather forecast (next 15 days)
- daily climate forecast (next 10 months)
- daily air quality forecast (next 5 days)
- get latitude and longitude from given city names
- get nearest city for given latitude and longitude

## Usage

Assume you have an `.env` file with the following content:

```env
GEOCODING_API_KEY=
HOURLY_WEATHER_API_KEY=
DAILY_WEATHER_API_KEY=R
DAILY_CLIMATE_API_KEY=
AIR_QUALITY_API_KEY=
OPENAI_API_KEY=
```

Note that you only need the API keys if you need the services.

```python
from llama_index.tools.measurespace import MeasureSpaceToolSpec
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_keys = {
    "hourly_weather": os.getenv("HOURLY_WEATHER_API_KEY"),
    "daily_weather": os.getenv("DAILY_WEATHER_API_KEY"),
    "daily_climate": os.getenv("DAILY_CLIMATE_API_KEY"),
    "air_quality": os.getenv("AIR_QUALITY_API_KEY"),
    "geocoding": os.getenv("GEOCODING_API_KEY"),
}

tool_spec = MeasureSpaceToolSpec(api_keys)
agent = FunctionAgent(
    tools=tool_spec.to_tool_list(),
    llm=OpenAI(model="gpt-4.1"),
)

print(await agent.run("How's the temperature for New York in next 3 days?"))
print(await agent.run("What's the latitude and longitude of New York?"))

# get a list of tools
for tool in tool_spec.to_tool_list():
    print(tool.metadata.name)

# Use a specific tool
tool_spec.get_daily_weather_forecast("New York")
tool_spec.get_latitude_longitude_from_location("New York")
```
