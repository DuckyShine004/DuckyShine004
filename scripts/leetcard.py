import requests

from pathlib import Path

MAX_TIMEOUT = 60

LEETCARD_URL = "https://leetcard.jacoblin.cool/duckyshine004?theme=dark&font=JetBrains%20Mono&border=0&ext=contest"

LEETCARD_DIRECTORY = "assets/svg/leetcard"
LEETCARD_FILENAME = "leetcard.svg"


def download_svg(url):
    path = Path(LEETCARD_DIRECTORY) / LEETCARD_FILENAME

    response = requests.get(url, timeout=MAX_TIMEOUT)

    path.write_bytes(response.content)


def main():
    download_svg(LEETCARD_URL)


if __name__ == "__main__":
    main()
