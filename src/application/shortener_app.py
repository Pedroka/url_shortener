from urllib.parse import urlparse

def shortener_url(url:str) -> str:
    if is_url(url):
        print("Encurtando URL")
    else:
        print("Nao é uma URL")


def is_url(url: str) -> bool:
    try:
        urlparse(url)
        return True
    except ValueError:
        return False