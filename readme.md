# Code Base Structure
## Components
    Client Side buyer Interface
    Client Side Seller Interface
    Front End for Buyer
    Front End For Seller
    DataBase
## Framework
    Buyer side- Rest using Flask
    Seller Side- REST using Flask
    GRPC to interact with front end and database
    SOAp server for financial transaction
## Run Locally
    Start the flask server - run the run.py file
    Start the GRPC Server- grpc_server/onlineshopping.py run this
    Start the SOAP server- run soapServer/server.py

# DEPLOYING CODE TO GCP
    Create a two GCP instances for front end and back end
    Open a cloud shell/local terminal and ssh to one of those instances
    clone https://github.com/sukanyasaha007/distributed-system-assignment2 --branch sukanya/gcp-setup
    Set up database in another instance and create database using database.sql schema
    Open first instance set up the env file and follow steps mentioned in Run loaclly part above



1. Create a GCP instance
2. Open a cloud shell
3. sudo su then navigate to app folder
4. git clone https://github.com/sukanyasaha007/distributed-system-assignment2 --branch nmk
5. docker pull nmk12345/grpc-image:latest
6. docker run -dt -v $(pwd):/app image-id -p 5000:5000 
7. docker exec -it container-id bash

# Refernce
    Flask, GRPC documents
    UI Design and integration is learned from tutorial of Jamal Bugti
    link: https://www.youtube.com/playlist?list=PLYPlvTh05MsxJja9bzQCSTDu4hnEv5N_u
