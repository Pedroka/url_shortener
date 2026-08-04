from urllib.parse import urlparse
from snowflake_id_toolkit import TwitterSnowflakeIDGenerator
import base62

class IdGenerator:
    def __init__(self):
        self.client_id = TwitterSnowflakeIDGenerator(node_id=1)
        self.id = self.id_generator()

    def id_generator(self):
        return self.client_id.generate_next_id()
    
    def encode_base62(self):
        return base62.encode(self.id)

    

def shortener_url(url:str) -> str:
    print(url)
    if is_url(url):
        generator = IdGenerator()
        base62_url = generator.encode_base62()
        
        return f'localhost:8000/{base62_url}'
    else:
        print("Nao é uma URL")


def is_url(url: str) -> bool:
    result = urlparse(url)
    return bool(result.scheme and result.netloc)