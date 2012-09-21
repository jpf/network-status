#filters output
import subprocess
from parse import parse_ping
from avg import cumulative_average
from termcolor import colored
import fileinput

cumulative = cumulative_average()
count = 0

def update(line):
  out = ''
  result = parse_ping(line)
  if result['status'] == 'got-reply':
    avg = cumulative.calculate(float(result['time']))
    color = 'blue'
    if avg > 100:
      color = 'yellow'
    if avg > 500:
      color = 'red'
    out = colored("%.2f" % (avg), color)
  elif result['success'] == False:
    out = colored(result['status'], 'red')

  # FIXME: Make this a rolling average?
  packet_loss = (1.0 - (float(cumulative.count + 1) / float(count))) * 100
  loss_color = 'blue'
  if packet_loss > 15:
    loss_color = 'yellow'
  if packet_loss > 50:
    loss_color = 'red'
  out_loss = colored("%.2f%%" % (packet_loss), loss_color)

  
  line_end = '\r'
  # line_end = '\n'
  # print "  %s (%.2f%%) [%d/%d] %s%s" % (out, packet_loss, cumulative.count, count,
  #                                   ' ' * 10, line_end),
  print "  %s (%s) %s%s" % (out, out_loss,
                                    ' ' * 10, line_end),

# for line in fileinput.input():
#   count += 1
#   update(line)
# print ""
# print ""

proc = subprocess.Popen(['ping','4.2.2.2'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
while True:
  count += 1
  line = proc.stdout.readline()
  if line == '':
    break
  update(line)

