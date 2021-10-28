import pyqrcode
import sys

s = sys.argv[1]
url = pyqrcode.create(s)
url.png(sys.argv[2], scale=6)
