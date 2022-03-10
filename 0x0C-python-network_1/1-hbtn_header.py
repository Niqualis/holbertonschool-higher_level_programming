#!/usr/bin/python3
"""url request that displays value of the variable X-Request-Id"""
if __name__ == '__main__':
    import urllib.parse
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print("{}".format(html.get('X-Request-ID')))
