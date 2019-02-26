# qREMS - Quality Room Environment Monitoring System

* This project is an implementation of flask, flask-socketio and socket.js

## Description
* __Quality Room Environment Monitoring System (qREMS)__ is a room-based environment monitoring system that uses a raspberry pi 3 as the host and temperature sensor, humidity sensor and barometer to collect the data for a given environment.
* Users in the same network as the raspberry pi can view the conditions in real time by going to the local IP address of the raspberry pi

## Usage
* clone this repository ``` git clone https://github.com/dertrockx/qREMS.git ```
* __using virtualenvironemnts__
   * do ``` pip install -r requirements.txt ```
* Using pipenv
   * do ``` pipenv install -r requirements.txt ```

## Running
* do ``` python app.py ```
