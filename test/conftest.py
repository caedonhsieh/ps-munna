from pathlib import Path

import pytest

import munna


TEST_ASSETS_DIR = Path(__file__).parent / 'assets'


###############################################################################
# Pytest fixtures
###############################################################################


@pytest.fixture(scope='session')
def dataset():
    """Preload the dataset"""
    return munna.Dataset('DATASET', 'valid')


@pytest.fixture(scope='session')
def datamodule():
    """Preload the datamodule"""
    return munna.DataModule('DATASET', batch_size=4, num_workers=0)


@pytest.fixture(scope='session')
def model():
    """Preload the model"""
    return munna.Model()
