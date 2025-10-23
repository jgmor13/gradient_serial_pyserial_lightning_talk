**Introduction and Background**
pySerial is a Python library that provides a simple and efficient way to access serial ports, enabling communication with hardware devices such as microcontrollers. This makes it particularly helpful for bridging Python code with the physical world, allowing developers to interact with embedded systems without needing to switch to lower-level languages like C for basic operations.

**Why PySerial is Helpful**
It facilitates communication with microcontrollers and other serial devices, enabling tasks like reading sensor data or controlling actuators directly from Python scripts.
This eliminates the need for language conversions when prototyping or automating hardware interactions, speeding up development in projects involving the Internet of Things (IoT), robotics, or custom electronics.

**History**
pySerial was originally created by Chris Liechti in 2001 as a Python extension for serial port access across multiple platforms. The project has evolved over the years, with releases like version 3.4 available as of 2020.

**License**
pySerial is released under the BSD-3-Clause license, which allows for free use, modification, and distribution with minimal restrictions. It is maintained under an open source license on GitHub.

**Industries Supported**
- Manufacturing
- Industry Automotive
- Robotics

**Installation / Implementation**
```bash
pip install pyserial
```
```python
import serial
```

Key functionality:

open/close
```python
__init__( port = 'COMX', baudrate = 9600, bytesize= EIGHTBITS,
parity = PARITY_NONE, stopbits = STOPBITS_ONE, timeout = NONE)

open() # Opens the serial port

is_open() # Returns True if port is open / False if port is closed

close() # Closes the serial port
```

Read Lines
```python 
read(size = 1) #Reads up to *size* byte

readline(size = 1) #Read and return one line in bytes

read_until(expected=b'\n' , size = None) #Reads serial in until expected 
```

Write Lines
```python
write(data) #write bytes to port

write_timeout() #Read or set the max amount of time a program will wait before timeout
```

Port
```python
get_settings() #Returns a dictionary of port settings

name() #Returns device name

baudrate() #Returns device baudrate

bytesize() #Returns byte size setting as an int
```

Buffer Management
```python
flush() #Clears buffer of file

reset_input_buffer() # Flush the input buffer

reset_ouptut_buffer() # Flush the output buffer

in_waiting() # Returns bytes in receive buffer

out_waiting() # Returns bytes in output buffer
```
