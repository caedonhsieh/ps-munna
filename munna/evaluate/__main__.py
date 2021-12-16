"""__main__.py - entry point for munna.evaluate"""


import argparse
from pathlib import Path

import munna


###############################################################################
# Entry point
###############################################################################


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dataset',
        help='The name of the dataset to evaluate')
    parser.add_argument(
        'partition',
        help='The partition to evaluate',
        default='valid')
    parser.add_argument(
        'checkpoint',
        type=Path,
        help='The checkpoint file to evaluate')
    parser.add_argument(
        'file',
        type=Path,
        help='The file to write results to')

    return parser.parse_args()


def main():
    """Evaluate a model"""
    # Parse command-line arguments
    args = parse_args()

    # Setup model
    model = munna.Model.load_from_checkpoint(args.checkpoint)

    # Evaluate
    munna.evaluate.dataset_to_file(args.dataset,
                                  args.partition,
                                  model,
                                  args.file)


if __name__ == '__main__':
    main()
