#!/usr/bin/python3
"""fetches URL of https://intranet.hbtn.io/status"""
if __name__ == '__main__':
    import urllib.request
    import urllib.parse

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as reply:
        html = reply.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
        