# Topology for NPA assignment 2c)
# Run with
# sudo mn --custom ./topo-2c.py --topo mytopo

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI


class MyTopo(Topo):
    def build(self):
        hosts = []
        switches = []

        # Add pod switches
        for pod in range(4):
            switches.append([self.addSwitch(f's{pod}{i}') for i in range(4)])
        
        # Add hosts
        for group in range(4):
            hosts.append([self.addHost(f'h{group}{i}') for i in range(4)])

        # Add backbone switches
        switches.append([self.addSwitch(f's4{i}') for i in range(4)])

        # Add links
        for pod in range(4):
            # Connect hosts with bottom switches
            self.addLink(hosts[pod][0], switches[pod][0])
            self.addLink(hosts[pod][1], switches[pod][0])
            self.addLink(hosts[pod][2], switches[pod][1])
            self.addLink(hosts[pod][3], switches[pod][1])
            
            # Connect bottom switches with top switches
            self.addLink(switches[pod][0], switches[pod][2])
            self.addLink(switches[pod][0], switches[pod][3])
            self.addLink(switches[pod][1], switches[pod][2])
            self.addLink(switches[pod][1], switches[pod][3])

        # Connect top switches with backbone switches
        for pod in range(4):
            self.addLink(switches[pod][2], switches[4][0])
            self.addLink(switches[pod][2], switches[4][1])
            self.addLink(switches[pod][3], switches[4][2])
            self.addLink(switches[pod][3], switches[4][3])

def main():
    net = Mininet(topo=MyTopo())
    net.start()

    CLI(net)

    net.stop()

if __name__ == '__main__':
    main()

topos = {
    'mytopo': ( lambda: MyTopo() )
}
