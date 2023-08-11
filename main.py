from src.testbed_client import TestBedClient
import signal
import sys


def print_command_mappings(commands: dict):
    print("Command Mappings:")
    for command, function in commands.items():
        print(f"{command}: {function.__name__}")

def handler_stop_signals(signum, frame):
    print('handler')
    sys.exit()




def main():
    client = TestBedClient()
    
    command_mappings = {
        '1': client.get_xyz_angular_velocity,
        '2': client.get_xyz_acceleration,
        '3': client.get_all,
        '4': client.get_attitude,
        '5': client.reset_attitude,
        '6': client.test_sensor,
        '7': client.test_connection,
    }

    signal.signal(signal.SIGTERM, handler_stop_signals)
    
    if not client.connect():
        print("Failed to connect to server.")
        client.close()
        sys.exit()

    print_command_mappings(command_mappings)

    try:
        while True:
            command = input("Enter a number or 'q' to quit: ")

            if command.lower() == 'q':
                break
            
            function = command_mappings.get(command)
            if function:
                res = function()
                print(res)
            else:
                print("Invalid input.")

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except Exception as e:
        print(e)
    finally:
        client.close()
        sys.exit()


if __name__ == "__main__":
    main()