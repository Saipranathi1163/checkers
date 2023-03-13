import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

port = 12345

s.bind((host, port))
s.listen(5)
print("conection initiated")
client, addr = s.accept()  # white client
print("conection ok")
client2, addr2 = s.accept()  # black client


def win_check(chess_board):
    if not (any('wk' in sublist for sublist in chess_board)):
        return 2
    elif not (any('bk' in sublist for sublist in chess_board)):
        return 1
    else:
        return 0


while True:
    msg = client.recv(4096)  # recieve Board from WHITE

    # check if white wins
    msg1 = pickle.loads(msg)
    print(winCheck(msg1))

    client2.send(msg)  # send the board to black(client2)
    client2.send(pickle.dumps(winCheck(msg1)))

    msg = client2.recv(4096)  # recieve the board from black (client 2)
    msg1 = pickle.loads(msg)
    # check if black wins

    client.send(msg)  # send it to White (client 1)
    client.send(pickle.dumps(winCheck(msg1)))
