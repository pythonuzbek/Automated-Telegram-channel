from abc import ABC, abstractmethod
from typing import Dict, List

import httpx
from fake_useragent import FakeUserAgent
from bs4 import BeautifulSoup

from new_sources.types import News


class BaseNewsSource(ABC):
    def __init__(self, url: str):
        self.parsed_source = BeautifulSoup(
            httpx.get(
                url=url,
                headers=self._get_headers()
            ).content,
            features='lxml'
        )
    @staticmethod
    def _get_headers() -> Dict:
        ua = FakeUserAgent()

        return {
            'User-Agent' : ua.random
        }

    def get_news(self) -> List[News]:
        raw_news = self._get_raw_today_news()
        return self._map_raw_news(raw_news=raw_news)


    @abstractmethod
    def _get_raw_today_news(self) -> List[BeautifulSoup]:
        pass

    @abstractmethod
    def _map_raw_news(self, raw_news: List[BeautifulSoup]) -> List[News]:
        pass

    @abstractmethod
    def _get_article_url(self, raw_news: BeautifulSoup) -> str:
        pass
    def _get_article_soup(self, raw_news: BeautifulSoup) -> BeautifulSoup:
        article_url = self._get_article_url(raw_news=raw_news)
        return BeautifulSoup(
            httpx.get(
                url=article_url,
                headers=self._get_headers()
            ).content,
            features='lxml'
        )

    @abstractmethod
    def _get_title(self, article_soup: BeautifulSoup) -> str:
        pass

    @abstractmethod
    def _get_summary(self, article_soup: BeautifulSoup) -> str:
        pass

    @abstractmethod
    def _get_img_url(self, article_soup: BeautifulSoup) -> str:
        pass
