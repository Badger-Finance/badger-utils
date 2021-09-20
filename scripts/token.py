#!/usr/bin/python3

from brownie import Token
from brownie import accounts


def main():
    return Token.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0]})
