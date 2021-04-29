# Add raftos package to PYTHONPATH so we don't need to install it to run example
# export PYTHONPATH="${PYTHONPATH}:$(pwd)/../"pip install raftos

# Remove previous data
rm -f *.log
rm -f *.storage
rm -f *.state_machine

# Start
python node.py --node "10.0.0.35" --cluster "5000 5000 5000" &
python node.py --node "10.0.0.36" --cluster "5000 5000 5000" &
python node.py --node "10.0.0.37" --cluster "5000 5000 5000" &

