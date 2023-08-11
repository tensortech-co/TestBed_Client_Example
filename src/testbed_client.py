from src.commands import ACECommand as Command
from src.singleton_meta import SingletonMeta

import socket

HEADER = 64
PORT = 5050
FORMAT = 'ascii'
SERVER = "192.168.0.228"
ADDR = (SERVER, PORT)
TIMEOUT = 1



class TestBedClient(metaclass=SingletonMeta):
    """
    A class that represents a client for the TestBed.

    Attributes:
        OK (int): A constant that represents a successful response from the TestBed.
        ERROR (int): A constant that represents an error response from the TestBed.
    """

    def __init__(self) -> None:
        self._isConnected = False
        self.client = self.create_client()
        self.OK = 1
        self.ERROR = -1

    def create_client(self):
        """
        Creates a new socket client for the testbed.

        Returns:
            A new socket client for the testbed.
        """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        client.settimeout(TIMEOUT)
        return client
    
    @property
    def is_connected(self):
        """
        Returns True if the client is currently connected to the testbed, False otherwise.
        """
        return self._isConnected

    def test_connection(self):
        """
        Tests the connection to the testbed and returns True if successful, False otherwise.
        """
        try:
            self.send(Command.test_connection)
            if self.receive() == str(self.OK):
                self._isConnected = True
                return True
            self._isConnected = False
            return False
        except:
            self._isConnected = False
            return False

    def connect(self) -> bool:
        # Test the connection first, if it's already connected, return True
        if self.test_connection():
            print("It's already connected.")
            return True

        try:
            self.client = self.create_client()
            self.client.connect(ADDR)
            self.test_connection()
            return self._isConnected
        except:
            print("Connect failed.")
            self._isConnected = False
            return self._isConnected
    
    def close(self):
        """
        Closes the connection to the testbed.
        """
        try:
            self.client.shutdown(1)
            self.client.close()
            self._isConnected = False
        except Exception as e:
            print(e)

    def send(self, msgToSend: str):
        msgToSend += "\r\n"
        message = msgToSend.encode(FORMAT)
        msgLength = len(message)
        sendLength = str(msgLength).encode(FORMAT)
        sendLength += b' ' * (HEADER - len(sendLength))
        self.client.send(sendLength)
        self.client.send(message)

    def receive(self) -> str:
        recvLength = self.client.recv(HEADER).decode(FORMAT)
        if recvLength:
            recvLength = int(recvLength)
            recvMsg = self.client.recv(recvLength).decode(FORMAT)
            recvMsg = recvMsg[:-2]
            return recvMsg
        else:
            self._isConnected = False
            raise socket.timeout("Server disconnect")

    def get_xyz_angular_velocity(self):
        self.send(Command.get_gyroscope)
        return [float(x) for x in self.receive().split(',')]
    

    def get_xyz_acceleration(self):
        self.send(Command.get_accelerometer)
        return [float(x) for x in self.receive().split(',')]
    
    
    def get_all(self):
        self.send(Command.get_all)
        return self.receive()
    

    def get_attitude(self):
        self.send(Command.get_attitude)
        return self.receive()
    
    def reset_attitude(self):
        self.send(Command.reset_attitude)
        return self.receive()
    
    def test_sensor(self):
        self.send(Command.test_sensor)
        return self.receive()
