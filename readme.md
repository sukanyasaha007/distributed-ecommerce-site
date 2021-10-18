# Code Base Structure
## Components
    1. Client Side Buyer Interface
    2. Client Side Seller Interface
    3. Front end for Buyer
    4. Front end For Seller
    5. DataBase

![Untitled](/images/assignment%202%20architechture.png)
## Framework
    1. Buyer side- REST using Flask
    2. Seller Side- REST using Flask
    3. GRPC to interact with database
    4. SOAp server for financial transaction

## Features
    1. Seller Side-
        1. Register
        2. Login
        3. Logout
        4. Add Product
        5. Update Product
        6. Delete Product
        7. Diplay current products and rating
    2. Buyer Side-
        1. Register
        2. Login
        3. Logout
        4. Search
        5. Add to Cart
        6. Remove/Update cart
        7. Display Cart
        8. Make Payment
        9. Provide Feedback
        10. Order History
## Run Locally
    1. Start the flask server - run the run.py file
    2. Start the GRPC Server- grpc_server/onlineshopping.py run this
    3. Start the SOAP server- run soapServer/server.py

# Deploy to GCP
    1. Create a two GCP instances for front end and back end
    2. Ope a local terminal and ssh to one of those instances
    3. Install python packages using pip and requirement.txt
    4. clone https://github.com/sukanyasaha007/distributed-system-assignment2 --branch sukanya/gcp-setup
    5. Set up database in another instance and create database using database.sql schema
    6. Open first instance set up the env file and follow steps mentioned in Run loaclly part above
    7. check latency report
# Refernce
    1. Flask, GRPC documents
    2. UI Design and integration is learned from tutorial of Jamal Bugti
    link: https://www.youtube.com/playlist?list=PLYPlvTh05MsxJja9bzQCSTDu4hnEv5N_u



