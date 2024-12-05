import os

from sympy import N

import src.const as const
from src.const import DOWNLOAD_DIR, INDEXES_DIR

def check_dirs()->None:
    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)
    os.chdir(DOWNLOAD_DIR)

    if not os.path.exists(INDEXES_DIR):
        os.mkdir(INDEXES_DIR)

#TODO: Check all of the capabilities of the system, and which models can be used
def check_requirements():
    const.SYSTEM_CAPABILITIES=None

# Helper function to run the setup
def run_setup()->None:
    check_dirs()
    check_requirements()