"""__main__.py - entry point for munna.preprocess"""


import argparse

import munna


###############################################################################
# Entry point
###############################################################################


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dataset',
        help='The name of the dataset to preprocess')
    return parser.parse_args()


if __name__ == '__main__':
    munna.preprocess.dataset(**vars(parse_args()))
