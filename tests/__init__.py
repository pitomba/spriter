import os


class Openned(object):
    code = 200

    def __init__(self, url):
        self.path = url

    def read(self):
        with open("tests/fixtures/%s" % os.path.basename(self.path)) as arq:
            content = arq.read()
        return content
