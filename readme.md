UI Design and integration is learned from tutorial of Jamal Bugti

link: https://www.youtube.com/playlist?list=PLYPlvTh05MsxJja9bzQCSTDu4hnEv5N_u

JWT - JSON Web Token

Seller Routes
POST /seller 201
GET /seller (rating + items sold + profile information)
POST /seller/session
DELETE /seller/session

POST /seller/product
GET /seller/product
GET /seller/product/:id
PATCH /seller/product/:id
DELETE /seller/product/:id

/buyer

{
    data: {
        itemsSold: [
            {
                productID: 123,
                ProductName: 'Abcd',
                qtySold: 5,
            },
                        {
                productID: 123,
                ProductName: 'Abcd',
                qtySold: 5,
            }
        ],
        profile: {
            name: "Abc seller",
            email: "abc@example.com",
            rating: 2.5,
        }
    }
}

{
    errors: [
        {
            title: 'Product not found',
            code: 'E001'
            message: 'The request producted does ...................'
        }
    ]
}


register
Login
add products
update products
delete products
view products
items sold
seller's rating display

CRUD operations



buyer

register
Login

#DEPLOYING CODE TO GCP

1. Create a GCP instance
2. Open a cloud shell
3. sudo su then navigate to app folder
4. git clone https://github.com/sukanyasaha007/distributed-system-assignment2 --branch nmk
5. docker pull nmk12345/grpc-image:latest
6. docker run -dt -v $(pwd):/app image-id -p 5000:5000 
7. docker exec -it container-id bash
