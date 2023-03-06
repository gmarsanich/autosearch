# Autosearch

Searches Google for a term and returns the first 10 results, but can be changed to however many you want/need

### How to use

0. Run `pip install google-api-python-client` to install the Google API client
1. Create a Goole API key
2. Create a Google Custom Search Engine
3. Create a file called key.toml with the following structure (or hardcode the API key and CSE ID into the program):
   ```
    [access]
    api_key = "your_api_key"
    cx = "your_cse_id"
   ```
4. All done!
