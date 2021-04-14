# Add raftos package to PYTHONPATH so we don't need to install it to run example
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../"

# Remove previous data
rm -f *.log
rm -f *.storage
rm -f *.state_machine

# Start
python node.py --node "10.0.0.26:25262" --cluster "10.0.0.26:25262 10.0.0.27:25262 10.0.0.28:25262" &
python node.py --node "10.0.0.27:25262" --cluster "10.0.0.26:25262 10.0.0.27:25262 10.0.0.28:25262" &
python node.py --node "10.0.0.28:25262" --cluster "10.0.0.26:25262 10.0.0.27:25262 10.0.0.28:25262" &
