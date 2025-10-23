import serial
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Initialize serial port
ser = serial.Serial(
    port='COM6',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)

# Data Storage
max_points = 100
data = []

#Plot Class
class Plot:
    def __init__(self):
        plt.ion()  #Interactive Mode
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.ax.set_title("Real-Time Serial Data")
        self.ax.set_xlabel("X-Axis")
        self.ax.set_ylabel("Y-Axis")
        self.ax.set_xlim(0, max_points)
        self.ax.set_ylim(0, 100)

        #continue to run condition
        self.running = True
        
        #Define Stop button
        self.fig.subplots_adjust(bottom=0.2)
        self.button_ax = self.fig.add_axes([0.80, 0.05, 0.1, 0.075]) 
        self.button = Button(self.button_ax, 'Stop')
        self.button.on_clicked(self.stop)

    #method to update interactive plot
    def update(self, data): self.line.set_data(range(len(data)), data)

    #call to stop plotting
    def stop(self, event): self.running = False

# plot object 
data_stream = Plot()

#main loop
while data_stream.running:
    #check for available data
    if ser.in_waiting > 0:
        #grab new line of data from arduino and decode
        serial_line = ser.read_until().decode().strip()
        if serial_line:
            print(serial_line)
            #strip distance tag and store as a float
            colon_idx = serial_line.find(":")
            data.append(float(serial_line[colon_idx+1:].strip()))
            #keep data buffer at 100 points
            if len(data) > max_points:  data.pop(0)
            #update data
            data_stream.update(data)
            plt.draw(); plt.pause(0.01)

ser.close()
plt.close()