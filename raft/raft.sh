# single node mode
cockroach start-single-node --insecure --listen-addr=0.0.0.0:26257 --http-addr=0.0.0.0:8080 --background


#multi node
# step 1 for all nodes-----
    cockroach start --insecure --listen-addr=0.0.0.0:25262 --http-addr=0.0.0.0:8080 --advertise-addr=10.0.0.37 --join=10.0.0.37:25262,10.0.0.35:25262,10.0.0.36:25262 --background

    cockroach start --insecure --listen-addr=0.0.0.0:25262 --http-addr=0.0.0.0:8080 --advertise-addr=10.0.0.35 --join=10.0.0.37:25262,10.0.0.35:25262,10.0.0.36:25262 --background

    cockroach start --insecure --listen-addr=0.0.0.0:25262 --http-addr=0.0.0.0:8080 --advertise-addr=10.0.0.36 --join=10.0.0.37:25262,10.0.0.35:25262,10.0.0.36:25262 --background

# step2 for all nodes
    cockroach init --insecure --host=0.0.0.0:25262
    cockroach sql --insecure --host=0.0.0.0:25262

# to quit
    cockroach quit --insecure --host=localhost:25262
# set up zone
SET CLUSTER SETTING server.remote_debugging.mode = 'any';

import mysqldump 'https://storage.googleapis.com/ds-assignment-storage/assignment4_20210331.sql';