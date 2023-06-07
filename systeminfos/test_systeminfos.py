"""
psutil Doc: https://psutil.readthedocs.io/en/latest/
"""
import psutil
from psutil._common import bytes2human
from time import sleep

print(psutil.cpu_times())

# gives a single float value
sleep(0.1)
print(psutil.cpu_percent(interval=None, percpu=True))
sleep(0.1)
print(psutil.cpu_percent(interval=None, percpu=True))
print(psutil.cpu_percent(interval=None, percpu=False))

# cpu count
print('cpus logical', psutil.cpu_count(logical=True))
print('cpus physical',psutil.cpu_count(logical=False))

print('cpu frequenz', psutil.cpu_freq(percpu=True))

print('load', psutil.getloadavg())

# gives an object with many fields
print(psutil.virtual_memory())

# you can convert that object to a dictionary
infos = dict(psutil.virtual_memory()._asdict())
print('mem total', infos['total'])
print('mem available', infos['available'])
print('mem percent', infos['percent'])
print('mem used', infos['used'])
print('mem free', infos['free'])

# you can have the percentage of used RAM
#print('used ram', psutil.virtual_memory().percent)

# you can calculate percentage of available memory
print('mem percent free', psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)


#####################
print('disk_usage', psutil.disk_usage('/'))

######### netstat #################
print('net', psutil.net_io_counters(pernic=True, nowrap=True))
print('net', psutil.net_io_counters(pernic=False, nowrap=True))


net_b = psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv
sleep(1)
net_a = psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv

print('bytes_recv', bytes2human( net_a - net_b, format="%(value).1f %(symbol)s") + '/s')


