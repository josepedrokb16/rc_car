import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GLib, GstRtspServer

HOST = "0.0.0.0"
PORT = 8559

PIPELINE = ("v4l2src device=/dev/video0 ! video/x-h264,width=1280,height=720,framerate=30/1 ! h264parse ! rtph264pay name=pay0 pt=96 sync=false "
            "alsasrc device=hw:1,0 ! audioconvert ! audioresample ! voaacenc ! rtpmp4apay name=pay1 pt=97")

print(f"hosting RTSP on {HOST}:{PORT}")
print(f"pipeline: {PIPELINE}")

# Initialize GStreamer
Gst.init(None)

# Create the RTSP server and set the port
server = GstRtspServer.RTSPServer()
server.props.service = str(PORT)

# Get the mount points to map URLs to media factories
mounts = server.get_mount_points()

# Create factory that will generate pipelines
factory = GstRtspServer.RTSPMediaFactory()
factory.set_launch(PIPELINE)

mounts.add_factory("/test", factory)
# Start listening for connections
server.attach(None)

# Create a GLib Main Loop and run it
loop = GLib.MainLoop()
try:
    loop.run()
except KeyboardInterrupt:
    pass
