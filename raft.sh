# single node mode
cockroach start-single-node --insecure --listen-addr=0.0.0.0:26257 --http-addr=0.0.0.0:8080 --background


#multi node
# step 1 for all nodes-----
    cockroach start --insecure --listen-addr=0.0.0.0:25262 --http-addr=0.0.0.0:8080 --advertise-addr=10.0.0.26 --join=10.0.0.26:25262,10.0.0.27:25262,10.0.0.28:25262 --background

    cockroach start --insecure --listen-addr=0.0.0.0:25262 --http-addr=0.0.0.0:8080 --advertise-addr=10.0.0.27 --join=10.0.0.26:25262,10.0.0.27:25262,10.0.0.28:25262 --background

    cockroach start --insecure --listen-addr=0.0.0.0:25262 --http-addr=0.0.0.0:8080 --advertise-addr=10.0.0.28 --join=10.0.0.26:25262,10.0.0.27:25262,10.0.0.28:25262 --background

# step2 for all nodes

    cockroach init --insecure --host=0.0.0.0:25262
    cockroach sql --insecure --host=0.0.0.0:25262

# to quit
    cockroach quit --insecure --host=localhost:25262
set up zone