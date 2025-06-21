import argparse
from main import createParser


def test_percer():
    res = createParser()
    assert type(res) == argparse.ArgumentParser
