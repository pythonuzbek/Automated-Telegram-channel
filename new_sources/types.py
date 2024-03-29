from dataclasses import dataclass

@dataclass
class News:
    title: str
    summary: str
    img_url: str

@dataclass
class NYTimesNews(News):
    pass