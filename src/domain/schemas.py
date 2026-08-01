import pydantic


class UrlShortener(pydantic.BaseModel):
    url: str