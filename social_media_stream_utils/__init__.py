import sys
from subprocess import Popen, PIPE

p = Popen([sys.executable, "-m", "playwright", "install"], stdin=PIPE, stdout=PIPE, stderr=PIPE)