stats = {}
with open('/proc/meminfo', 'r') as f:
    for line in f:
        parts = line.split(":")
        stats[parts[0].strip()] = parts[1].split()[0].strip()
print(float(stats['MemFree'])/float(stats['MemTotal']))

