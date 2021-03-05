# Code Base Structure
## Components
    1. Client Side Buyer Interface
    2. Client Side Seller Interface
    3. Front end for Buyer
    4. Front end For Seller
    5. DataBase
## Framework
    1. Buyer side- Rest using Flask
    2. Seller Side- REST using Flask
    3. GRPC to interact with database
    4. SOAp server for financial transaction
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
# Refernce
    1. Flask, GRPC documents
    2. UI Design and integration is learned from tutorial of Jamal Bugti
    link: https://www.youtube.com/playlist?list=PLYPlvTh05MsxJja9bzQCSTDu4hnEv5N_u
