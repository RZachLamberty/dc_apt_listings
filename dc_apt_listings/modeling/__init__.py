#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: __init__.py
Author: zlamberty
Created: 2015-07-18

Description:
    modeling of apartment data in Washington, DC

Usage:
    <usage>

"""

import argparse
import logging
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

logger = logging.getLogger(__name__)


# ----------------------------- #
#   Main routine                #
# ----------------------------- #

def main():
    """ docstring """
    pass


# ----------------------------- #
#   Command line                #
# ----------------------------- #

def parse_args():
    """ Take a log file from the commmand line """
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--xample", help="An Example", action='store_true')

    args = parser.parse_args()

    logger.debug("arguments set to {}".format(vars(args)))

    return args


if __name__ == '__main__':

    args = parse_args()

    main()
