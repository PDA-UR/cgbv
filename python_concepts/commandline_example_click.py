#!/usr/bin/env python3

import click

@click.command()
@click.argument('filename')
@click.option('--scale', default=3, type=int, help='Scale Factor')
def process(filename, scale):
    print(f"Opening {filename}...")  # f-String for inserting variables into string
    print("Scaling %s to %dx size... " % (filename, scale))  # %() method for inserting variables into string

if __name__ == "__main__":
    process()
