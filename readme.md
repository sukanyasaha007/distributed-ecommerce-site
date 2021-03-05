# Code Base Structure
## Components
    Client Side Buyer Interface
    Client Side Seller Interface
    Front end for Buyer
    Front end For Seller
    DataBase
## Framework
    Buyer side- Rest using Flask
    Seller Side- REST using Flask
    GRPC to interact with database
    SOAp server for financial transaction
## Run Locally
    Start the flask server - run the run.py file
    Start the GRPC Server- grpc_server/onlineshopping.py run this
    Start the SOAP server- run soapServer/server.py

# Deploy to GCP
    1. Create a two GCP instances for front end and back end
    2. Ope a local terminal and ssh to one of those instances
    3. Install python packages using pip and requirement.txt
    4. clone https://github.com/sukanyasaha007/distributed-system-assignment2 --branch sukanya/gcp-setup
    5. Set up database in another instance and create database using database.sql schema
    6. Open first instance set up the env file and follow steps mentioned in Run loaclly part above
# Refernce
    Flask, GRPC documents
    UI Design and integration is learned from tutorial of Jamal Bugti
    link: https://www.youtube.com/playlist?list=PLYPlvTh05MsxJja9bzQCSTDu4hnEv5N_u
