from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

def topology():
    net = Mininet(controller=RemoteController)
    c0 = net.addController('c0', port=6653)
    # Add hosts and switches
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()