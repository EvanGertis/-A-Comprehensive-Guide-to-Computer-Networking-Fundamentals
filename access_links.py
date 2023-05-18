import random
import time

# Define the number of devices
num_devices = 3

# Define the time duration of each transmission
transmission_duration = 1  # in seconds

# Define the probability of collision
collision_probability = 0.2

# Loop through the devices
for device_id in range(num_devices):
    # Wait for a random period of time before attempting to transmit
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    
    # Check if the channel is idle
    channel_idle = True
    for i in range(transmission_duration):
        # Check if the channel is busy
        if not channel_idle:
            print(f"Device {device_id + 1}: Transmission failed due to collision")
            break
        
        # Check if another device is transmitting
        for j in range(num_devices):
            if j == device_id:
                continue
            transmit_time = i + wait_time
            if transmit_time >= j and transmit_time < j + transmission_duration:
                channel_idle = False
                break
        
        # Transmit the message if the channel is idle
        if channel_idle and i == transmission_duration - 1:
            print(f"Device {device_id + 1}: Transmission successful")