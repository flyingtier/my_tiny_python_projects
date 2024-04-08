#!/usr/bin/env python
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
#parser.add_argument('name', help='Name to greet')
parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
args = parser.parse_args()

print('Hello, ' + args.name + '!')

