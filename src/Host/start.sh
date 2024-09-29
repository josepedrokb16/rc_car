source /home/rpi/rc_car/src/Host/venv/bin/activate
export PYTHONPATH=/home/rpi/rc_car/src
uvicorn main:app --host 0.0.0.0 --port 8000 --reload