#!/usr/bin/env python

import click

@click.command()
def hello():
    click.echo('HELLO WORLD')
    
if __name__ == '__main__':
    hello()