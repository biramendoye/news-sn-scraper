import re
from bs4 import BeautifulSoup
from .utils import log, get_selectors
from requests.adapters import HTTPAdapter


@log
def send_request(_url: str, _session):
    """Make an http request to a given url with request"""
    REQUEST_TIMEOUT = 5
    MAX_RETRIES = 3
    SUCCESS = 200
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0"
    }

    _session.mount(prefix='https://', adapter=HTTPAdapter(max_retries=MAX_RETRIES))
    _response = _session.get(_url, headers=headers, timeout=REQUEST_TIMEOUT)
    if _response.status_code == SUCCESS:
        return _response.content
    else:
        return None


@log
def extract_links_from_senego(_html_content):
    """Extract from HTML page article links from senego.com"""
    selectors = get_selectors('senego')
    a_tag, a_class = selectors['news'].split('.')
    soup = BeautifulSoup(_html_content, "lxml")
    links = soup.find_all(a_tag, attrs={'class': a_class})

    return [l.get('href') for l in links]


@log
def extract_links_from_seneweb(_html_content):
    soup = BeautifulSoup(_html_content, "lxml")

    all_links = soup.find_all(href=re.compile(".html"))
    all_links = [l.get('href') for l in all_links] 
    all_links = [l for l in all_links if l.startswith('/news')] # we remove external links
    all_links = [f"https://seneweb.com{l}" for l in all_links]

    return all_links