from flask import Flask, request, render_template
from flask_socketio import SocketIO
from threading import Thread, Event
import random
from time import sleep

app = Flask(__name__)
socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()

class DataThread(Thread):
	def __init__(self):
		self.delay = 1
		super(DataThread, self).__init__()

	def Generate(self):
		print("Making random number")
		while not thread_stop_event.isSet():
			humidity = float(random.randint(1, 100) * random.randint(1,5) / random.randint(5, 20))
			temperature = float(random.randint(1, 100) * random.randint(1,5) / random.randint(5, 20))
			pressure = float(random.randint(1, 100) * random.randint(1,5) / random.randint(5, 20))
			data = {
				'humidity': humidity,
				'temperature': temperature,
				'pressure': pressure
			}
			socketio.emit('changeData', data)
			sleep(self.delay)
	def run(self):
		self.Generate()

	def stop(self):
		thread_stop_event.set()

@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('connect')
def connect():
	global thread
	print("Starting thread")
	if not thread.isAlive():
		thread = DataThread()
		thread.start()


	

if __name__ == '__main__':
	app.run(debug=True)