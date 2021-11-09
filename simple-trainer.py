# trainer.py
from collections import Counter
import socket
import sys
import time
import ray
from pprint import pprint

num_cpus = int(sys.argv[1])
addr = sys.argv[2]
redispw = sys.argv[3]


ray.init(address=addr, _redis_password=redispw)
print('''This cluster consists of
         {} nodes in total
         {} CPU resources in total'''.format(len(ray.nodes()), ray.cluster_resources()['CPU']))

print("All node data:")
pprint(ray.nodes(), indent=4)
pprint(ray.cluster_resources(), indent=4)


@ray.remote
def f():
    time.sleep(1)
    return socket.gethostbyname(socket.gethostname())


# The following takes one second (assuming that
# ray was able to access all of the allocated nodes).
for i in range(60):
    start = time.time()
    ip_addresses = ray.get([f.remote() for _ in range(num_cpus)])
    print(Counter(ip_addresses))
    end = time.time()
    print(end - start)
