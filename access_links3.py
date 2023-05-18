import numpy as np

# Define the spreading codes for each device
spreading_codes = np.array([
    [1, -1, -1, 1],
    [1, 1, -1, -1],
    [-1, 1, 1, -1],
])

# Define the messages to be sent by each device
messages = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
])

# Encode the messages using the spreading codes
encoded_messages = np.dot(messages, spreading_codes)

# Transmit the encoded messages over the channel
channel = np.sum(encoded_messages, axis=0)

# Decode the messages using the spreading codes
decoded_messages = np.dot(channel, spreading_codes.T)

# Print the decoded messages
print("Decoded messages:", decoded_messages)