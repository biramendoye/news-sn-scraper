import argparse


def cli():
    parser = argparse.ArgumentParser(epilog="python main --name senego", add_help=True)

    parser.add_argument(
        "--name",
        type=str,
        help="The name of the website",
        required=True,
    )

    return parser.parse_args()