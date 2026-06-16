---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-weather/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-weather/README.md
---
# Weather Loader

```bash
pip install llama-index-readers-weather
```

This loader fetches the weather data from the OpenWeatherMap's OneCall API, using the `pyowm` Python package. You must initialize the loader with your OpenWeatherMap API token, and then pass in the names of the cities you want the weather data for.

OWM's One Call API provides the following weather data for any geographical coordinate: - Current weather - Hourly forecast for 48 hours - Daily forecast for 7 days

## Usage

To use this loader, you need to pass in an array of city names (eg. [chennai, chicago]). Pass in the country codes as well for better accuracy.

```python
from llama_index.readers.weather import WeatherReader

loader = WeatherReader(token="[YOUR_TOKEN]")
documents = loader.load_data(places=["Chennai, IN", "Dublin, IE"])
```

This loader is designed to be used as a way to load data into LlamaIndex.
