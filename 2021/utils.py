import os

import requests
from dotenv.main import find_dotenv
from dotenv import load_dotenv

def read_aoc_data(day: int) -> str:
    load_dotenv(find_dotenv())

    r = requests.get(
        f"https://adventofcode.com/2021/day/{day}/input",
        cookies={'session': os.environ.get("session")}
    )

    r.raise_for_status()
    
    return r.content.decode('ascii')