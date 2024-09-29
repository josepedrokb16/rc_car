sudo cp cam.service /etc/systemd/system
sudo cp car.service /etc/systemd/system

sudo systemctl daemon-reload

sudo systemctl enable cam
sudo systemctl enable car

sudo systemctl start cam
sudo systemctl start car