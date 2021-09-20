# Code Base Structure
## Components
    1. Client Side Buyer Interface
    2. Client Side Seller Interface
    3. Front end for Buyer
    4. Front end For Seller
    5. DataBase
<img src= "assignment 2 architechture.png" alt="architecture" />
## Framework
    1. Buyer side- Rest using Flask
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

senario 4:

                             time(sec)
request                               
addTocart                     0.755756
admin_login                   0.113434
buyerCreateAccount           20.320010
buyer_login                   0.575088
clearcart                     0.270097
deleteItem                    0.259238
getFinalOrder                 0.119419
getHomePage                   0.655471
getProductDetails             0.220980
getcart                       0.386134
getorder                      0.522506
seller_cat                    0.111393
seller_landing_page_loading   0.179129
seller_products_view          0.130059
updateProduct                 0.230755
updatedCart                   0.286707
userLogout                    0.393769


senario 1

getHomePage,0.627694845199585
getHomePage,0.548072099685669
getcart,0.3926420211791992
getorder,0.5505561828613281
getFinalOrder,0.10475015640258789
getFinalOrder,0.10554313659667969
getFinalOrder,0.10593199729919434
getFinalOrder,0.10568022727966309
getFinalOrder,0.10814404487609863
getFinalOrder,0.10859894752502441
getcart,0.3889899253845215
buyer_login,0.111846923828125
getHomePage,0.5701019763946533
getcart,0.3678419589996338
clearcart,0.2500147819519043
getHomePage,0.5711560249328613
getHomePage,0.5297391414642334
getcart,0.41370606422424316
clearcart,0.27355432510375977
getHomePage,0.6044340133666992
getcart,0.4526519775390625
getorder,0.6301259994506836
getFinalOrder,0.10308718681335449
getFinalOrder,0.1037912368774414
getFinalOrder,0.10397696495056152

senario 2

seller_landing_page_loading,0.1975250244140625
seller_landing_page_loading,0.17226600646972656
seller_landing_page_loading,0.16323494911193848
getHomePage,0.19920086860656738
getHomePage,0.1963798999786377
seller_landing_page_loading,0.18327927589416504
seller_landing_page_loading,0.1601238250732422
seller_landing_page_loading,0.19555306434631348
getHomePage,0.20342707633972168
buyer_login,0.10277485847473145
buyer_login,0.12487506866455078
seller_landing_page_loading,0.1912672519683838
seller_landing_page_loading,0.1711280345916748
admin_login,0.117919921875
seller_landing_page_loading,0.19587993621826172
admin_login,0.10943794250488281
seller_landing_page_loading,0.1640779972076416
updateProduct,0.2366352081298828
seller_landing_page_loading,0.17089295387268066
seller_landing_page_loading,0.16324806213378906
seller_landing_page_loading,0.16600298881530762
seller_landing_page_loading,0.15635299682617188
seller_cat,0.11139321327209473
seller_landing_page_loading,0.16231608390808105
seller_products_view,0.13005900382995605
seller_landing_page_loading,0.17449021339416504


senario 3

buyer_login,0.013024568557739258
getHomePage,0.10080766677856445
addTocart,0.09741854667663574
getHomePage,0.09279632568359375
getcart,0.07080793380737305
getcart,0.07708215713500977
getHomePage,0.09679770469665527
displayOrders,0.0436098575592041
displayOrders,0.050583839416503906
displayOrders,0.057782888412475586
displayOrders,0.06493043899536133
displayOrders,0.07114291191101074
displayOrders,0.08436298370361328
displayOrders,0.09091067314147949
rateSeller,0.017519474029541016
displayOrders,0.02238750457763672
displayOrders,0.02896857261657715
displayOrders,0.03559684753417969
displayOrders,0.04154610633850098
displayOrders,0.048166751861572266
displayOrders,0.059857845306396484
displayOrders,0.06641292572021484
getHomePage,0.1013181209564209
getHomePage,0.09808135032653809
getcart,0.07458996772766113
getorder,0.09749746322631836


