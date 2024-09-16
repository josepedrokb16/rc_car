# RC_CAR with a Raspberry Pi
# Gstreamer libraries
sudo apt update
sudo apt install gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-rtsp

# Python bindings
sudo apt-get install python3-gst-1.0 gir1.2-gst-rtsp-server-1.0

# Python libraries
pip3 install PyGObject

You might have to run the python script as sudo to access the camera.
