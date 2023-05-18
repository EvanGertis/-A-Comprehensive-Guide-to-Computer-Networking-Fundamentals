from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI

# Create the network topology
net = Mininet(controller=Controller, switch=OVSKernelSwitch)
c0 = net.addController('c0')
s1 = net.addSwitch('s1')
h1 = net.addHost('h1', ip='10.0.0.1')
h2 = net.addHost('h2', ip='10.0.0.2')
net.addLink(h1, s1)
net.addLink(h2, s1)

# Start the network
net.start()

# Ping the second host from the first host
h1.cmd('ping -c 3 10.0.0.2')

# Disable the link between the first host and the switch
net.configLinkStatus('h1', 's1', 'down')

# Ping the second host from the first host again
h1.cmd('ping -c 3 10.0.0.2')

# Enable the link between the first host and the switch
net.configLinkStatus('h1', 's1', 'up')

# Ping the second host from the first host once more
h1.cmd('ping -c 3 10.0.0.2')

# Stop the network
net.stop()