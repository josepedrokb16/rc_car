import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GLib, GstRtspServer

HOST = "0.0.0.0"
PORT = 8559
PIPELINE = 'v4l2src ! videorate ! video/x-raw,framerate=30/1 ! videoconvert ! queue ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast key-int-max=15 ! queue ! rtph264pay name=pay0 pt=96 sync=false'

print(f"hosting RTSP on {HOST}:{PORT}")
print(f"pipeline: {PIPELINE}")

# Initialize GStreamer
Gst.init(None)

# Create the GStreamer pipeline description
pipeline_description = (PIPELINE)

# Create the RTSP server
server = GstRtspServer.RTSPServer()
server.props.service = str(PORT)
mounts = server.get_mount_points()
factory = GstRtspServer.RTSPMediaFactory()
factory.set_launch(pipeline_description)
factory.set_shared(True)
mounts.add_factory("/test", factory)
server.attach(None)

# Create a GLib Main Loop and run it
loop = GLib.MainLoop()
try:
    loop.run()
except KeyboardInterrupt:
    pass