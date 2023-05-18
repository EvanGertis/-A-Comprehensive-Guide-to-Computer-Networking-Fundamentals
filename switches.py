import NetworkManager

# Get the list of available Ethernet connections
ethernet_connections = NetworkManager.Settings.ListConnections()
print("Available Ethernet connections:")
for connection in ethernet_connections:
    connection_type = connection.GetSettings()['connection']['type']
    if connection_type == '802-3-ethernet':
        ethernet_device = NetworkManager.Devices[connection.GetSettings()['connection']['device']]
        print(ethernet_device.Interface)

# Connect to an Ethernet connection
ethernet_connection = ethernet_connections[0]
if ethernet_connection:
    connection_settings = ethernet_connection.GetSettings()
    connection_settings['connection']['id'] = 'My Ethernet Connection'
    connection_settings['802-3-ethernet']['mac-address'] = ethernet_device.HwAddress
    connection = NetworkManager.Settings.AddConnection(connection_settings)
    NetworkManager.NetworkManager.ActivateConnection(connection, ethernet_device, "/")

    print("Connected to Ethernet connection:", ethernet_device.Interface)