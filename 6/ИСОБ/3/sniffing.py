
from scapy.all import *





if __name__ == '__main__':             # example

    t = AsyncSniffer(count = 50)
    t.start()
    t.join()
    results = t.results
    print(results)


