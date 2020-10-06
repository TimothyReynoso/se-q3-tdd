#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Timothy Reynoso"


import sys
import argparse

print(sys.argv)


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="Echo Clone")
    # your code here
    parser.add_argument('input')
    parser.add_argument(
        '-u', '--upper', action="store_true", help='hello => HELLO')
    parser.add_argument(
        '-l', '--lower', action="store_true", help="HELLO => hello")
    parser.add_argument(
        '-t', '--title', action="store_true", help="hello => Hello")
    return parser


def main(args):
    """Implementation of echo"""
    # your code here
    parser = create_parser()

    ns = parser.parse_args()

    if ns.lower:
        print(ns.input.lower())
        return ns.input.lower()
    elif ns.upper:
        print(ns.input.upper())
        return ns.input.upper()
    elif ns.title:
        print(ns.input.title())
        return ns.input.title()
    else:
        print(ns.input)
        return ns.input


if __name__ == '__main__':
    main(sys.argv[1:])
