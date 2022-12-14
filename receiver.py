import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.bind(('', 64345))

print("Receiver is ready!")

while True:
    data, addr = s1.recvfrom(2048)
    
    readOffset = 0
    nameLen = int.from_bytes(data[readOffset:readOffset+4], byteorder='big')
    readOffset += 4

    name = data[readOffset:readOffset+nameLen].decode("utf-16")
    readOffset += nameLen

    messageLen = int.from_bytes(data[readOffset:readOffset+4], byteorder='big')
    readOffset += 4

    message = data[readOffset:readOffset+messageLen].decode("utf-16")
    readOffset += messageLen

    print(f"<{name}> {message}")