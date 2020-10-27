#!/usr/bin/env python3

"""
Random number generation using the random.org API
"""

import requests
import json


def true_random_numbers(numbers, minimum, maximum, api_key, random_url="https://api.random.org/json-rpc/2/invoke"):
    """
    Generates a true random number, or list of numbers, using the random.org API

    Parameters
    ----------
    numbers: int (range: [1, 1e4])
        Number of random numbers to generate
    minimum: int
        Smallest int to return
    maximum:
        Largest int to return
    api_key: str
        User API Key from random.org
    random_url: str (default is current version 2 API)
        API base URL

    Returns
    -------
    Union[int,list]
        If 1 random number requested, return an int. If multiple requested, return a list of ints
    """
    if minimum >= maximum:
        raise ValueError(f"Maximum ({maximum}) must be greater minimum ({minimum})")
    if numbers < 1:
        raise ValueError(f"At least 1 random number must be requested")
    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {"apiKey": api_key, "n": int(numbers), "min": int(minimum), "max": int(maximum), "replacement": True},
        "id": 24601,
    }
    headers = {"content-type": "application/json"}
    response = requests.post(random_url, data=json.dumps(payload), headers=headers)
    data = json.loads(response.text)["result"]["random"]["data"]
    if len(data) == 1:
        return data[0]
    else:
        return data


if __name__ == "__main__":
    with open("random_org_key") as F:
        random_org_api_key = F.read().strip()
    print(true_random_numbers(1, 1, 2, random_org_api_key))
