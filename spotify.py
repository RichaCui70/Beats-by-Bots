import serial
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

DEVICE_ID="b03c89af01a60a74e51fb8f511f93afec9e9a9d8"
CLIENT_ID="0091c9b455d647689272268875bfc164"
CLIENT_SECRET="e6dc87d2f1e24a02a2f9e1ac802c965c"

arduino_port = "COM3"
baud_rate = 9600

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-playback-state,user-modify-playback-state"))
    
# create an infinite while loop that will always be waiting for a new scan
try:
    ser = serial.Serial(arduino_port, baud_rate)
    while True:
        rfid = ser.readline().decode('utf-8').strip()    
        print("Card Value is:",rfid)
        sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
        if (rfid == "90EF9020"):
            # playing a song
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1yYlpGuBiRRf33e1gY61bN'])
                
        elif (rfid=='A06C2320'):
            # playing an album
            sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:01jpNkrvSof31UUJk2kLif')      
        # continue adding as many "elifs" for songs/albums that you want to play
except Exception as e:
    print(f"Error: {e}")