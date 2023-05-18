import socket
import pickle

# Sender code
def sender(window_size, timeout, data, dest_ip, dest_port):
    # Create a UDP socket for sending data
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender_socket.settimeout(timeout)

    # Set the initial sequence number and the base of the window
    seq_num = 0
    base = 0

    # Split the data into packets of size = window_size
    packets = [data[i:i+window_size] for i in range(0, len(data), window_size)]

    while base < len(packets):
        # Send packets within the window
        for i in range(base, min(base+window_size, len(packets))):
            packet = (seq_num, packets[i])
            sender_socket.sendto(pickle.dumps(packet), (dest_ip, dest_port))
            print("Sent packet with sequence number:", seq_num)
            seq_num += 1

        try:
            # Receive ACKs for all packets within the window
            while True:
                ack_packet, server_address = sender_socket.recvfrom(4096)
                ack = pickle.loads(ack_packet)
                if ack >= base:
                    print("Received ACK for packet with sequence number:", ack)
                    base = ack + 1
        except socket.timeout:
            # Timeout, resend packets in the window
            print("Timeout occurred, resending packets with sequence numbers:", base, "to", seq_num-1)
            seq_num = base

    # Close the socket
    sender_socket.close()

# Receiver code
def receiver(window_size, timeout, dest_ip, dest_port):
    # Create a UDP socket for receiving data
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_socket.bind((dest_ip, dest_port))
    receiver_socket.settimeout(timeout)

    # Set the expected sequence number
    expected_seq_num = 0

    while True:
        try:
            # Receive packets and send ACKs
            data_packet, client_address = receiver_socket.recvfrom(4096)
            packet = pickle.loads(data_packet)
            seq_num = packet[0]
            if seq_num == expected_seq_num:
                print("Received packet with sequence number:", seq_num)
                receiver_socket.sendto(pickle.dumps(seq_num), client_address)
                expected_seq_num += 1
            else:
                print("Received packet with out-of-order sequence number:", seq_num)
                receiver_socket.sendto(pickle.dumps(expected_seq_num-1), client_address)
        except socket.timeout:
            # Timeout, assume all packets have been received
            break

    # Close the socket
    receiver_socket.close()
# You can use the sender() function to send data over th