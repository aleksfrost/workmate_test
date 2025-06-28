import argparse


def createParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--where")
    parser.add_argument("--aggregate")
    parser.add_argument("--order-by")

    return parser