from sys import platform, exit
from glob import glob
from serial import Serial
from pynput.keyboard import Key, Controller


def serial_ports():
    """Thanks, Thomas!
    https://stackoverflow.com/questions/12090503
    """
    if platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif platform.startswith('linux') or platform.startswith('cygwin'):
        ports = glob('/dev/tty[A-Za-z]*')
    elif platform.startswith('darwin'):
        ports = glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unknown platform')
    return ports


def reader(port):
    serial = Serial(port, 9600)
    keyboard = Controller()
    data = serial.readline().decode('utf-8').strip()
    while data:
        if data == 'jump':
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif data == 'duck':
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        data = serial.readline().decode('utf-8').strip()


def cli():
    print(r"""
              ____  _                 __      _
             / __ \(_)___  ____  ____/ /_  __(_)___  ____
            / / / / / __ \/ __ \/ __  / / / / / __ \/ __ \
           / /_/ / / / / / /_/ / /_/ / /_/ / / / / / /_/ /
          /_____/_/_/ /_/\____/\__,_/\__,_/_/_/ /_/\____/
                                                          """)
    print("version 0.1 by renmans on " + platform)
    ports = serial_ports()
    command = input("Enter serial port or type 'list' to display" +
                    " all available serial ports: ")
    if command == 'list':
        for num, port in enumerate(ports):
            print('[{:02}] '.format(num) + port)
        port_num = input("Choose serial port: ")
        try:
            port = ports[int(port_num)]
        except KeyError:
            print('[ERROR] Wrong serial port number.')
            exit()
    else:
        if command in ports:
            port = command
        else:
            print('[ERROR] No such serial port.')
            exit()
    return port


if __name__ == '__main__':
    try:
        port = cli()
        reader(port)
    except KeyboardInterrupt:
        exit()
