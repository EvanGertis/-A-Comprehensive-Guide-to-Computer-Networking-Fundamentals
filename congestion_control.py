# Define variables
threshold = 10
window_size = 1
cwnd = 1
ssthresh = 100
# Loop through packets
for packet in packets:
    # Check if congestion has occurred
    if packet.loss == True:
        # Reduce window size and set threshold
        ssthresh = max(cwnd/2, 2)
        cwnd = 1
        window_size = 1
    else:
        # Increase window size
        window_size += 1 if window_size >= cwnd:
        # Increase congestion window size
    if cwnd < ssthresh:
        cwnd += 1 
    else:
        cwnd += 1/cwnd