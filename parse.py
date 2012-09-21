import re
import fileinput

def parse_ping(line):
    reply = re.compile('^(\d+) bytes from ([0-9\.]+): icmp_seq=(\d+) ttl=(\d+) time=(\d+\.\d+) ms')
    # 64 bytes from 4.2.2.2: icmp_seq=269 ttl=57 time=33.817 ms
    if 'bytes from' in line:
        match = reply.match(line)
        results = match.groups()
        result = {
            'success': True,
            'error': False,
            'bytes': results[0],
            'from_ip': results[1],
            'icmp_seq': results[2],
            'ttl': results[3],
            'time': results[4],
            'status': 'got-reply'
            }
    elif 'Request timeout for' in line:
        result = {
            'success': False,
            'error': False,
            'status': 'timeout'
            }
    elif 'PING ' in line:
        result = {
            'success': True,
            'error': False,
            'status': 'ping-started'
            }
    elif 'sendto: Network is down' in line:
        result = {
            'success': False,
            'error': False,
            'status': 'network-down'
            }
    elif 'sendto: No route to host' in line:
        result = {
            'success': False,
            'error': False,
            'status': 'no-route'
            }
    else:
        result = {
            'error': True,
            'success': False,
            'status': '[UNRECOGNIZED LINE] ' + line
            }
    return result

if __name__ == '__main__':
    for line in fileinput.input():
        rv = parse_ping(line)
        if rv['error']:
            print rv['status'],

