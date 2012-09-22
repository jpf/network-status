# -*- coding: utf-8 -*-
#filters output
import subprocess
from parse import parse_ping
from avg import cumulative_average, windowed_average
from termcolor import colored
import fileinput

trend_icon = {
  'up': u'↑',
  'up-slightly': u'↗',
  'flat': ' ',
  'down-slightly': u'↘',
  'down': u'↓'
}

class trending:
  def __init__(self, window):
    self.historical_avg = windowed_average(window)
    self.avg = windowed_average(int(window / 3))
    self.value = 0
    self.historical_value = 0
    self.trend = 1
    
  def update(self, value):
    self.value = self.avg.calculate(value)
    self.historical_value = self.historical_avg.calculate(value)
    self.trend = float(self.value) / float(self.historical_value)

  def icon(self):
    trend = self.trend
    # print 'trend: ' + str(trend)
    if trend > 1.6:
      return trend_icon['up']
    if trend > 1.2:
      return trend_icon['up-slightly']
    if trend <= 1.2 and trend >= 0.8:
      return trend_icon['flat']
    if trend < 0.8:
      return trend_icon['down-slightly']
    if trend < 0.2:
      return trend_icon['down']
    return '!'
    
      
window = 30
rtt_avg = windowed_average(window)
pl_avg = windowed_average(window)
trend = trending(window)

count = 0

def update(line):
  out = ''
  packet_loss = 0.0
  result = parse_ping(line)
  if result['status'] == 'got-reply':
    avg = rtt_avg.calculate(float(result['time']))
    packet_loss = pl_avg.calculate(1)
    trend.update(float(result['time']))
    if avg <= 100:
      color = 'blue'
    if avg > 100:
      color = 'yellow'
    if avg > 500:
      color = 'red'
    out = colored("%.2f" % (avg), color)
    trend.icon()
  elif result['success'] == False:
    out = colored(result['status'], 'red')
    packet_loss = pl_avg.calculate(0)
  if packet_loss <= 15:
    loss_color = 'blue'
  if packet_loss > 15:
    loss_color = 'yellow'
  if packet_loss > 50:
    loss_color = 'red'
  out_loss = colored("%.2f%%" % ((1 - packet_loss) * 100), loss_color)
  line_end = '\r'
  # print " %s (%.2f%%) [%d/%d] %s%s" % (out, packet_loss, cumulative.count, count,
  #                                   ' ' * 10, line_end),
  print " %s%s ms (%s) %s%s" % (trend.icon(), out, out_loss,
                                    ' ' * 10, line_end),

debug = False


if debug:
  for line in fileinput.input():
    count += 1
    update(line)
    print '\n',
  print ""
else:
  proc = subprocess.Popen(['ping','4.2.2.2'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  while True:
    count += 1
    line = proc.stdout.readline()
    if line == '':
      break
    update(line)
