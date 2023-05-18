import time

# Define the time slots and number of devices
time_slots = 4
num_devices = 3

# Define the messages to be sent by each device
messages = ['Hello from device 1', 'Hello from device 2', 'Hello from device 3']

# Define the time duration of each time slot
time_slot_duration = 1  # in seconds

# Loop through the time slots and devices
for time_slot in range(time_slots):
    print(f"Time slot {time_slot + 1}:")
    for device_id in range(num_devices):
        # Calculate the start and end times for the device's time slot
        start_time = time_slot + (device_id * time_slots)
        end_time = start_time + 1
        
        # Send the message during the device's time slot
        if time.time() >= start_time and time.time() < end_time:
            print(f"Device {device_id + 1}: Sending message '{messages[device_id]}'")