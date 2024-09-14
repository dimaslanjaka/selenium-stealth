import json
import os
import random
import tempfile
from typing import Any, Dict, Union
from requests_cache import CachedSession
from .utils import write_json_file, md5, read_json_file

# Define the filename and the path to the %TEMP% directory
temp_dir = os.path.join(tempfile.gettempdir(), "fp")
os.makedirs(temp_dir, exist_ok=True)  # Create the directory if it doesn't exist


def fetch_fingerprint():
    # URL and parameters
    url = "https://fingerprints.bablosoft.com/preview"
    # https://fingerprints.bablosoft.com/prepare?tags=Chrome,Microsoft&key=
    params = {
        "rand": "0.8730723602904835",
        "tags": "Chrome,Microsoft Windows",
        "maxWidth": "1366",
        "maxHeight": "768",
        "perfectCanvasLogs": "true",
        "key": "",
    }

    # Headers
    headers = {
        "Host": "fingerprints.bablosoft.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Origin": "https://fp.bablosoft.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://fp.bablosoft.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=0",
        "Pragma": "no-cache",
    }

    # Keep responses for [n] seconds
    session = CachedSession("tmp/fingerprint-getter", expire_after=60)
    # Make the GET request
    response = session.get(url=url, headers=headers, params=params, verify=False)
    response_text = response.text
    if response_text:
        file_path = os.path.join(temp_dir, str(md5(response_text)) + ".json")
        write_json_file(file_path, json.loads(response_text))
    return response_text


def get_cached_fingerprint() -> Union[Dict[str, Any], None]:
    # Get a list of files in the temp_dir
    files = [
        f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))
    ]

    # Check if there are any files in the directory
    if files:
        # Select a random file
        random_file = random.choice(files)
        random_file_path = os.path.join(temp_dir, random_file)
        return read_json_file(random_file_path)  # type: ignore
    return None


if __name__ == "__main__":
    print(json.loads(fetch_fingerprint()))
