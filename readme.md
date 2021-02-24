/


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

