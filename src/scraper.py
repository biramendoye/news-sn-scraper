from datetime import date, timedelta
from .crawler import (extract_links_from_senego, extract_links_from_seneweb, send_request)


def scraper_for_senego(session, db):
    BASE_URL = "https://senego.com/page/"
    MAX_PAGE = 13901
    for i in range(1, 3):
        content = send_request(BASE_URL + str(i), session)
        post_urls = extract_links_from_senego(content)
        post_urls = [(p,) for p in post_urls]
        db.save_url(post_urls)
    db.connection.close()


def scraper_for_seneweb_new_content(session, db):
    urls = [
            "https://seneweb.com/news/politique/",
            "https://seneweb.com/news/videos/",
            "https://seneweb.com/news/societe/",
            "https://seneweb.com/news/religion/",
            "https://seneweb.com/news/sport/",
            "https://seneweb.com/news/afrique/",
            "https://seneweb.com/news/people/",
        ]
    for url in urls:
        content = send_request(url, session)
        post_urls = extract_links_from_seneweb(content)
        post_urls = [(p,) for p in post_urls]
        db.save_url(post_urls)
    db.connection.close()

def scraper_for_seneweb_old_content(session, db):
    # for old links we start from the year 2010 to 2019
    start = date(2010, 1, 1)
    end = date(2019, 12, 31)
    BASE_URL = "https://seneweb.com/news/retronews/"
    delta = timedelta(days=1)
    while start <= end:
        post_date = start.strftime("%d-%m-%Y")
        start += delta
        content = send_request(BASE_URL + post_date, session)
        post_urls = extract_links_from_seneweb(content)
        post_urls = [(p,) for p in post_urls]
        db.save_url(post_urls)
    db.connection.close()