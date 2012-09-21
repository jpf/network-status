#filters output
import subprocess
from parse import parse_ping

proc = subprocess.Popen(['ping','4.2.2.2'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
elements = []
count = 0
ma = 0.0
while True:
  line = proc.stdout.readline()
  if line != '':
    result = parse_ping(line)
    if result['status'] == 'got-reply':
        count += 1
        time = float(result['time'])
        elements.append(time)
        ma = float(ma + (time - ma) / count)
        avg = sum(elements) / len(elements)
        print "test: %s\t%f\t%f" % (result['time'], avg, ma)
  else:
    break
