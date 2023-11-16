# SpotifyArduino

## Description

A program that uses Spotify API, an RFID scanner and card, an Arduino, as well as a device with Spotify downloaded to play certain songs or songs from an album or playlist via RFID cards

## Installation

Download a code editor, as well as the Arduino IDE

## Usage

Upload the .ino file to the Arduino using the Arduino IDE. Be sure you have the right COM port as well as BAUD rate (default is 9600). 
In the .py file, make sure you change your CLIENT_SECRET, CLIENT_ID, DEVICE_ID to your specific app and device. Per RFID, you must get the song/album/playlist URI so that it could play it. Insert it after every if/elif statement.
Run the .py file by executing python spotify.py. Be sure your present working directory is aligned with where the .py file is.
```
python spotify.py
```

## Inspiration + Help

https://www.youtube.com/watch?v=-jGWjFR936o&ab_channel=talaexe
They used a Rasperry Pi to control playback. I modified the code such that it would read RFID outputs from serial communication. Ultimately watching their video helped alot. 

## License

Clearly state the license under which your code is released. Common licenses include MIT, Apache, GPL, etc.
