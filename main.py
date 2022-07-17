from requests import Session
from src.scraper import (scraper_for_senego, scraper_for_seneweb_new_content, scraper_for_seneweb_old_content)

from src.cli import cli
from src.db import DBPipeline


def main():
    session = Session()

    db = DBPipeline()
    db.create_table()

    args = cli()
    if args.name == "senego":
        scraper_for_senego(session, db)
    elif args.name == "seneweb":
        scraper_for_seneweb_new_content(session, db)
        # scraper_for_seneweb_old_content(session, db)
    else:
        print("Website not yet implemented!!")

    session.close()


if __name__ == "__main__":
    main()
