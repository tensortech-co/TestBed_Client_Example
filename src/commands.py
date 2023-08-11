class ACECommand:
    """
    A class that defines the commands that can be sent to the TestBed during the ACE mode.

    Attributes:
        get_gyroscope (str): The command to retrieve the angular velocity of the gyroscope.
        get_accelerometer (str): The command to retrieve the acceleration of the accelerometer.
        get_all (str): The command to retrieve all sensor data.
        get_attitude (str): The command to retrieve the attitude of the testbed.
        reset_attitude (str): The command to reset the attitude of the testbed.
        test_sensor (str): The command to test the sensor of the testbed.
        test_connection (str): The command to test the connection to the testbed.
    """
    get_gyroscope = "get gyroscope"
    get_accelerometer = "get accelerometer"
    get_all = "get all"
    get_attitude = "get attitude"
    reset_attitude = "reset attitude"
    test_sensor = "test sensor"
    test_connection = "test connection"