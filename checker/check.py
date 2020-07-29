#!/usr/bin/python3

import argparse
import os.path
import sys

import polib

from checker.BakuChecker import *


def init_checkr():
    dictFile = os.path.dirname(os.path.realpath(__file__))+"/dict.txt"
    checkerList = []
    checkerList.append(BakuChecker(dictFile))
    return checkerList


def usual_read(f):
    checkerList = init_checkr()

    for i in range(0, len(f)):
        errList = []
        if (f[i][len(f[i])-1] == "\n"):
            f[i] = f[i][:-1]

        for check in checkerList:
            result = check.check(f[i])
            result.line = i
            errList.append(result)

        return errList


def read_po(file_location):
    checkerList = init_checkr()

    po = polib.pofile(file_location)
    errList = []
    for entry in po:
        for check in checkerList:
            errList += check.check(entry.msgstr)
    return errList


def print_error(errList):
    for err in errList:
        print("Checker       : {}".format(err.checkerDescription))
        print("Line          : {}".format(err.line))
        print("Original text : {}".format(err.original))
        print("Message       : {}".format(err.message))
        print()
    print("Total Error: {}".format(len(errList)))


def print_error_po(errList):
    for err in errList:
        print("Checker       : {}".format(err.checkerDescription))
        print("Original text : {}".format(err.original))
        print("Message       : {}".format(err.message))
        print()
    print("Total Error: {}".format(len(errList)))


def main():
    print("#"*70)
    print("# Indonesian Kata Baku Checker for PO File" + " "*27 + "#")
    print("# Author   : Bervianto Leo Pratama" + " "*35 + "#")
    print("# Date     : December 12, 2018" + " "*39 + "#")
    print("#"*70)
    print()

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type')
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    if (len(sys.argv) < 2):
        print("Usage:")
        print("{} <path-to-file>".format(sys.argv[0]))
    else:
        if (not(os.path.exists(args.input))):
            print("File {} not found.".format(args.input))
        else:
            f = open(args.input).readlines()
            if (len(sys.argv) == 2):
                errList = usual_read(f)
                print_error(errList)
            else:
                type = args.type
                if (type == 'po'):
                    errList = read_po(args.input)
                    print_error_po(errList)
                else:
                    errList = usual_read(f)
                    print_error(errList)


if __name__ == "__main__":
    main()
