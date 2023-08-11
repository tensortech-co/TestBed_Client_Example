## TestBedClient
TestBedClient is a Python client for a testbed server that provides sensor data and allows users to send commands to the testbed. This client provides a command line interface that allows users to interact with the testbed server and retrieve sensor data.

### Installation
To install the TestBedClient, simply clone the repository:
```
git clone https://github.com/tensortech-co/TestBed_Client_Example.git
```

### Usage
To use the TestBedClient, simply run the main.py script:
```
python main.py
```

This will start the command line interface, which will prompt you to enter a command. You can enter a number corresponding to a command, or 'q' to quit the program.

The available commands are:
>
    1. Get XYZ angular velocity
    2. Get XYZ acceleration
    3. Get all sensor data
    4. Get attitude
    5. Reset attitude
    6. Test sensor
    7. Test connection