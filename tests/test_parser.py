import argparse
from args_parser import createParser


def test_percer():
    res = createParser()
    assert type(res) == argparse.ArgumentParser
