--
-- File generated with SQLiteStudio v3.3.0 on Wed Feb 24 15:25:13 2021
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: cart
CREATE TABLE cart (
	id INTEGER NOT NULL,
	name VARCHAR (80) NOT NULL,
	price NUMERIC (10, 2) NOT NULL,
	discount INTEGER,
	color TEXT NOT NULL,
	quantity INTEGER,
	image TEXT,
	colors TEXT
)
	stock INTEGER NOT NULL,
	desc TEXT NOT NULL,
	pub_date DATETIME NOT NULL,
	category_id INTEGER NOT NULL,
	brand_id INTEGER NOT NULL,
	image_1 VARCHAR (150) NOT NULL,
	image_2 VARCHAR (150) NOT NULL,
	image_3 VARCHAR (150) NOT NULL,
	condition TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY (category_id) REFERENCES category (id),
	FOREIGN KEY (brand_id) REFERENCES brand (id));


	-- Table: addproduct
	CREATE TABLE cart (
		id INTEGER NOT NULL,
		product_id INTEGER,
		customer_id INTEGER,
		name VARCHAR (80) NOT NULL,
		price NUMERIC (10, 2) NOT NULL,
		discount INTEGER,
		stock INTEGER NOT NULL,
		colors TEXT NOT NULL,
		descp TEXT NOT NULL,
		pub_date DATETIME NOT NULL,
		image_1 VARCHAR (150) NOT NULL,
		image_2 VARCHAR (150) NOT NULL,
		image_3 VARCHAR (150) NOT NULL,
		PRIMARY KEY (id)
	);

-- Table: addproduct
CREATE TABLE addproduct (
	id INTEGER NOT NULL,
	name VARCHAR (80) NOT NULL,
	price NUMERIC (10, 2) NOT NULL,
	discount INTEGER,
	stock INTEGER NOT NULL,
	colors TEXT NOT NULL,
	desc TEXT NOT NULL,
	pub_date DATETIME NOT NULL,
	category_id INTEGER NOT NULL,
	brand_id INTEGER NOT NULL,
	image_1 VARCHAR (150) NOT NULL,
	image_2 VARCHAR (150) NOT NULL,
	image_3 VARCHAR (150) NOT NULL,
	condition TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY (category_id) REFERENCES category (id),
	FOREIGN KEY (brand_id) REFERENCES brand (id));

INSERT INTO addproduct VALUES (1, 'macbook pro', 1200.99, 0, 12, 'gray,white,black,pink', 'In that case, the MacBook Pro is most certainly worth it because it may be the only laptop that can do the job. Plus, the MacBook Pro can also be configured to boot Windows if that is needed for certain software available only on Windows', '2020-02-16 19:48:54.706965', 2, 1, '492392c9a1d80c65f3c3.jpg', '68e0b733e736307b0cba.jpeg', '870b6e7fe62f69b1b811.jpeg', 'laptop', NULL);
INSERT INTO addproduct VALUES (2, 'iphone x', 1150.99, 0, 20, 'gray,white,black', 'In that case, the MacBook Pro is most certainly worth it because it may be the only laptop that can do the job. Plus, the MacBook Pro can also be configured to boot Windows if that is needed for certain software available only on Windows', '2020-02-16 20:09:14.716623', 1, 1, '1b6b45a578914ed1fde8.jpg', 'f7a5a4ca49273d1ca481.jpeg', 'adf5364b9edb107fcc91.jpg', 'phone', NULL);
INSERT INTO addproduct VALUES (3, 'imac', 1950.99, 10, 20, 'gray,white,black', 'In that case, the MacBook Pro is most certainly worth it because it may be the only laptop that can do the job. Plus, the MacBook Pro can also be configured to boot Windows if that is needed for certain software available only on Windows', '2020-02-16 20:10:19.765750', 3, 1, 'fcd9f839069f478205ca.jpeg', 'c3434dc04ae9b08a1a62.jpg', 'f0f100021cc040042e55.jpg', 'laptop', NULL);
INSERT INTO addproduct VALUES (4, 'sony laptop', 880.5, 15, 20, 'gray,white,black', 'In that case, the Sony is most certainly worth it because it may be the only laptop that can do the job. Plus, the Sony  can also be configured to boot Windows if that is needed for certain software available only on Windows', '2020-02-16 20:11:42.641343', 2, 2, '1a8f02a703d918008306.jpg', '64ee0289b5a406f5bcf9.jpg', '1bb91dfc4629c7adcd2c.jpg', 'laptop', NULL);
INSERT INTO addproduct VALUES (5, 'sony tv', 980.5, 0, 20, 'pink,gray,white,black,blue', 'In that case, the Sony is most certainly worth it because it may be the only laptop that can do the job. Plus, the Sony  can also be configured to boot Windows if that is needed for certain software available only on Windows', '2020-02-16 20:14:20.388327', 4, 2, '87fcab43cab157ab14b7.jpg', '34942c9898c611980859.jpg', '02448be8f85e3555bbd3.jpeg', 'tv', NULL);
INSERT INTO addproduct VALUES (6, 'sony mobile', 780.5, 10, 20, 'blue,gray,white,black', 'In that case, the Sony is most certainly worth it because it may be the only laptop that can do the job. Plus, the Sony  can also be configured to boot Windows if that is needed for certain software available only on Windows', '2020-02-16 20:15:54.494452', 1, 2, '040f3c7cb7d97ac64e6e.jpeg', '24929353ddc0bafa0446.jpg', '33db0031a633112aee3a.jpeg', 'phone', NULL);
INSERT INTO addproduct VALUES (7, 'HP', 780.5, 5, 20, 'blue,gray,white,black', 'In that case, the HP is most certainly worth it because it may be the only laptop that can do the job. Plus, the PH  can also be configured to boot Windows if that is needed for certain software available only on Windows', '2020-02-16 20:18:25.194836', 2, 4, 'fb152ad7428856fb1a92.jpg', 'f30553a2120ecde23684.jpeg', '397833603b0ea0762805.jpg', 'laptop', NULL);
INSERT INTO addproduct VALUES (8, 'Dell', 780.5, 5, 20, 'blue,gray,white,black', 'In that case, the HP is most certainly worth it because it may be the only laptop that can do the job. Plus, the PH  can also be configured to boot Windows if that is needed for certain software available only on Windows', '2020-02-16 20:19:50.257060', 2, 3, 'c8cd10e2fd79892fd1f1.jpeg', '7b3f6dcc218945581199.jpg', '16cfef10d24fe04f54ac.jpeg', 'lapop', NULL);
INSERT INTO addproduct VALUES (9, 'Samsang mobile', 780.5, 15, 25, 'blue,gray,white,black', 'In that case, the Samsang is most certainly worth it because it may be the only laptop that can do the job. Plus, the Samsang  can also be configured to boot Windows if that is needed for certain software available only on Windows', '2020-02-16 20:21:54.556674', 1, 6, 'b93a85f9a61f2a7856d8.png', '36506d32d97d01c298a1.jpeg', 'b691bc6172599269eed1.jpg', 'mobile', NULL);
INSERT INTO addproduct VALUES (10, 'Rado watch', 1200.99, 0, 25, 'golden,white,black', 'Millions of people around the world have - and continue to - improve their lives based on the teachings of Dale Carnegie. In "How to Win Friends and Influence People", Carnegie offers practical advice and techniques, in his exuberant and conversational style, for how to get out of a mental rut and make life more rewarding. His advice has stood the test of time and will teach you how to: make friends quickly and easily; increase your popularity', '2020-02-17 18:21:23.979112', 7, 5, 'b85904527fd0cea93c90.jpeg', 'c1c37e487199c78c64d3.jpg', 'ee42709e4fe53e241762.jpeg', 'watch', NULL);
INSERT INTO addproduct VALUES (11, 'Canon camera ', 560.89, 0, 25, 'gray,white,black', 'Millions of people around the world have - and continue to - improve their lives based on the teachings of Dale Carnegie. In "How to Win Friends and Influence People", Carnegie offers practical advice and techniques, in his exuberant and conversational style, for how to get out of a mental rut and make life more rewarding. His advice has stood the test of time and will teach you how to: make friends quickly and easily; increase your popularity', '2020-02-17 18:22:56.607738', 6, 7, 'dc900c380baf7d227ef0.png', '21b85a9bc4f7b8ef21fc.jpeg', '3e2be726a5b063a2cfe1.jpeg', 'camera', NULL);
INSERT INTO addproduct VALUES (12, 'Apple watch', 450.89, 10, 9, 'blue,gray,white,black', 'Millions of people around the world have - and continue to - improve their lives based on the teachings of Dale Carnegie. In "How to Win Friends and Influence People", Carnegie offers practical advice and techniques, in his exuberant and conversational style, for how to get out of a mental rut and make life more rewarding. His advice has stood the test of time and will teach you how to: make friends quickly and easily; increase your popularity', '2020-02-17 18:29:29.190442', 7, 1, '09f788f8cb89c480faa7.png', '87bf0baeab6af4239466.jpg', '62f2f68db7286cbbd58a.jpeg', 'watch', NULL);
INSERT INTO addproduct VALUES (13, 'Galaxy', 400, 10, 20, 'red', 'Sony Galaxy cheap good fast', '2021-02-20 19:20:01.299310', 3, 2, '21d278cd3fcbd593c7df.jpeg', 'fabaf16b5eb8f789c4b3.jpeg', '907de7caf1b8f84d8e69.jpeg', 'phone', NULL);
c
-- Table: alembic_version
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL,
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Table: brand
CREATE TABLE brand (
	id INTEGER NOT NULL,
	name VARCHAR(30) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (name)
);
INSERT INTO brand (id, name) VALUES (1, 'Apple');
INSERT INTO brand (id, name) VALUES (2, 'Sony');
INSERT INTO brand (id, name) VALUES (3, 'Dell');
INSERT INTO brand (id, name) VALUES (4, 'HP');
INSERT INTO brand (id, name) VALUES (5, 'Rado');
INSERT INTO brand (id, name) VALUES (6, 'samsung');
INSERT INTO brand (id, name) VALUES (7, 'Canon');

-- Table: category
CREATE TABLE category (
	id INTEGER NOT NULL,
	name VARCHAR(30) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (name)
);
INSERT INTO category (id, name) VALUES (1, 'Mobile');
INSERT INTO category (id, name) VALUES (2, 'Laptop');
INSERT INTO category (id, name) VALUES (3, 'Desktop');
INSERT INTO category (id, name) VALUES (4, 'TV');
INSERT INTO category (id, name) VALUES (5, 'Ipad');
INSERT INTO category (id, name) VALUES (6, 'Camera');
INSERT INTO category (id, name) VALUES (7, 'Watch');

-- Table: customer_order
CREATE TABLE customer_order (
	id INTEGER NOT NULL,
	invoice VARCHAR(20) NOT NULL,
	status VARCHAR(20) NOT NULL,
	customer_id INTEGER NOT NULL,
	date_created DATETIME NOT NULL,
	orders TEXT,
	PRIMARY KEY (id),
	UNIQUE (invoice)
);
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (1, '5cb3282fd9', 'Pending', 1, '2020-05-05 19:08:39.240926', '{"10": {"color": "golden", "colors": "golden,white,black", "discount": 0, "image": "b85904527fd0cea93c90.jpeg", "name": "Rado watch", "price": 1200.99, "quantity": 1}, "11": {"color": "gray", "colors": "gray,white,black", "discount": 0, "image": "dc900c380baf7d227ef0.png", "name": "Canon camera ", "price": 560.89, "quantity": 1}, "12": {"color": "blue", "colors": "blue,gray,white,black", "discount": 10, "image": "09f788f8cb89c480faa7.png", "name": "Apple watch", "price": 450.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (2, 'a6e8a7bf3b', 'Pending', 2, '2020-05-06 11:31:17.614707', '{"10": {"color": "golden", "colors": "golden,white,black", "discount": 0, "image": "b85904527fd0cea93c90.jpeg", "name": "Rado watch", "price": 1200.99, "quantity": 1}, "11": {"color": "gray", "colors": "gray,white,black", "discount": 0, "image": "dc900c380baf7d227ef0.png", "name": "Canon camera ", "price": 560.89, "quantity": 1}, "12": {"color": "blue", "colors": "blue,gray,white,black", "discount": 10, "image": "09f788f8cb89c480faa7.png", "name": "Apple watch", "price": 450.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (3, '2c1dba9580', 'Pending', 2, '2020-05-06 11:31:27.139262', '{"11": {"color": "gray", "colors": "gray,white,black", "discount": 0, "image": "dc900c380baf7d227ef0.png", "name": "Canon camera ", "price": 560.89, "quantity": 1}, "12": {"color": "blue", "colors": "blue,gray,white,black", "discount": 10, "image": "09f788f8cb89c480faa7.png", "name": "Apple watch", "price": 450.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (4, '09fefc3d3c', 'Pending', 2, '2020-05-06 11:36:27.669339', '{"10": {"color": "golden", "colors": "golden,white,black", "discount": 0, "image": "b85904527fd0cea93c90.jpeg", "name": "Rado watch", "price": 1200.99, "quantity": 1}, "12": {"color": "blue", "colors": "blue,gray,white,black", "discount": 10, "image": "09f788f8cb89c480faa7.png", "name": "Apple watch", "price": 450.89, "quantity": "2"}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (5, '9bb1b9c3d5', 'Pending', 2, '2020-05-06 11:39:05.303821', '{"10": {"color": "golden", "colors": "golden,white,black", "discount": 0, "image": "b85904527fd0cea93c90.jpeg", "name": "Rado watch", "price": 1200.99, "quantity": 1}, "11": {"color": "gray", "colors": "gray,white,black", "discount": 0, "image": "dc900c380baf7d227ef0.png", "name": "Canon camera ", "price": 560.89, "quantity": "2"}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (6, '31b57e2fef', 'Pending', 2, '2020-05-11 18:06:29.579892', '{"10": {"color": "golden", "colors": "golden,white,black", "discount": 0, "image": "b85904527fd0cea93c90.jpeg", "name": "Rado watch", "price": 1200.99, "quantity": 1}, "11": {"color": "gray", "colors": "gray,white,black", "discount": 0, "image": "dc900c380baf7d227ef0.png", "name": "Canon camera ", "price": 560.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (7, 'ebdbf60f1b', 'Paid', 2, '2020-05-11 18:42:51.527684', '{"10": {"color": "golden", "discount": 0, "name": "Rado watch", "price": 1200.99, "quantity": 1}, "12": {"color": "blue", "discount": 10, "name": "Apple watch", "price": 450.89, "quantity": 1}, "9": {"color": "blue", "discount": 15, "name": "Samsang mobile", "price": 780.5, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (8, '347bcdf796', 'Paid', 2, '2020-05-11 18:56:24.106484', '{"12": {"color": "blue", "discount": 10, "name": "Apple watch", "price": 450.89, "quantity": "1"}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (9, '49278fe361', 'Pending', 3, '2021-02-20 19:22:24.911728', '{"11": {"color": "gray", "colors": "gray,white,black", "discount": 0, "image": "dc900c380baf7d227ef0.png", "name": "Canon camera ", "price": 560.89, "quantity": 1}, "12": {"color": "blue", "colors": "blue,gray,white,black", "discount": 10, "image": "09f788f8cb89c480faa7.png", "name": "Apple watch", "price": 450.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (10, '32a3611a02', 'Pending', 3, '2021-02-20 19:29:43.278914', '{"13": {"color": "red", "colors": "red", "discount": 0, "image": "21d278cd3fcbd593c7df.jpeg", "name": "phone", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (11, 'daa115646f', 'Pending', 3, '2021-02-20 20:26:59.549665', '{"13": {"color": "red", "colors": "red", "discount": 0, "image": "21d278cd3fcbd593c7df.jpeg", "name": "phone", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (12, '66e99d657b', 'Pending', 3, '2021-02-20 23:15:16.392316', '{"13": {"color": "red", "colors": "red", "discount": 0, "image": "21d278cd3fcbd593c7df.jpeg", "name": "phone", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (13, 'f6f3e66e6d', 'Pending', 3, '2021-02-20 23:40:34.026956', '{"12": {"color": "blue", "colors": "blue,gray,white,black", "discount": 10, "image": "09f788f8cb89c480faa7.png", "name": "Apple watch", "price": 450.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (14, '572f1fed8d', 'Pending', 3, '2021-02-20 23:47:48.599834', '{"10": {"color": "golden", "colors": "golden,white,black", "discount": 0, "image": "b85904527fd0cea93c90.jpeg", "name": "Rado watch", "price": 1200.99, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (15, '5934b1a930', 'Pending', 3, '2021-02-20 23:53:03.149527', '{"12": {"color": "blue", "colors": "blue,gray,white,black", "discount": 10, "image": "09f788f8cb89c480faa7.png", "name": "Apple watch", "price": 450.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (16, 'd611e1fd00', 'Pending', 3, '2021-02-21 00:07:16.893970', '{"11": {"color": "gray", "colors": "gray,white,black", "discount": 0, "image": "dc900c380baf7d227ef0.png", "name": "Canon camera ", "price": 560.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (17, 'ec4926b0d2', 'Pending', 3, '2021-02-22 03:02:28.132630', '{"10": {"color": "golden", "colors": "golden,white,black", "discount": 0, "image": "b85904527fd0cea93c90.jpeg", "name": "Rado watch", "price": 1200.99, "quantity": 2}, "13": {"color": "red", "colors": "red", "discount": 0, "image": "21d278cd3fcbd593c7df.jpeg", "name": "phone", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (18, '57911d89ca', 'Pending', 3, '2021-02-22 16:44:22.999632', '{"12": {"color": "blue", "colors": "blue,gray,white,black", "discount": 10, "image": "09f788f8cb89c480faa7.png", "name": "Apple watch", "price": 450.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (19, 'b707747939', 'Paid', 3, '2021-02-22 16:46:24.053024', '{"13": {"color": "red", "colors": "red", "discount": 10, "image": "21d278cd3fcbd593c7df.jpeg", "name": "Galaxy", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (20, '52fa92c2f5', 'Paid', 3, '2021-02-22 17:13:10.520724', '{"13": {"color": "red", "colors": "red", "discount": 10, "image": "21d278cd3fcbd593c7df.jpeg", "name": "Galaxy", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (21, '81c9c6bb56', 'Paid', 3, '2021-02-22 17:35:50.460021', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (22, '98c4f68beb', 'Paid', 3, '2021-02-22 17:37:16.813821', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (23, 'da8c1b1b04', 'Paid', 3, '2021-02-22 17:38:06.149339', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (24, 'f9bc34c817', 'Paid', 3, '2021-02-22 17:39:41.477761', '{"13": {"color": "red", "colors": "red", "discount": 10, "image": "21d278cd3fcbd593c7df.jpeg", "name": "Galaxy", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (25, '6d9243cbfd', 'Paid', 3, '2021-02-22 17:41:02.448473', '{"13": {"color": "red", "colors": "red", "discount": 10, "image": "21d278cd3fcbd593c7df.jpeg", "name": "Galaxy", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (26, '2dc5024e4a', 'Paid', 3, '2021-02-22 17:42:26.770137', '{"12": {"color": "blue", "colors": "blue,gray,white,black", "discount": 10, "image": "09f788f8cb89c480faa7.png", "name": "Apple watch", "price": 450.89, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (27, '79c0329f49', 'Paid', 3, '2021-02-22 17:43:01.188775', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (28, 'dc4aa68378', 'Paid', 3, '2021-02-22 17:45:06.774554', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (29, 'e12023f448', 'Paid', 3, '2021-02-22 17:46:29.987421', '{"13": {"color": "red", "colors": "red", "discount": 10, "image": "21d278cd3fcbd593c7df.jpeg", "name": "Galaxy", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (30, '47c201ad4e', 'Paid', 3, '2021-02-22 17:47:40.105413', '{"13": {"color": "red", "colors": "red", "discount": 10, "image": "21d278cd3fcbd593c7df.jpeg", "name": "Galaxy", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (31, '4e9a3c3553', 'Paid', 3, '2021-02-22 17:51:22.859188', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (32, 'ed246fb795', 'Paid', 3, '2021-02-22 17:52:52.594649', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (33, 'dcc9bbe842', 'Paid', 3, '2021-02-22 17:53:38.067771', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (34, '37845d25d7', 'Paid', 3, '2021-02-22 17:55:15.471155', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (35, 'ae72ba2ac4', 'Paid', 3, '2021-02-22 17:57:01.033854', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (36, '0016a7f5c8', 'Paid', 3, '2021-02-22 17:58:06.874319', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (37, '526296e40f', 'Paid', 3, '2021-02-22 18:02:53.044796', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (38, 'd84463f260', 'Paid', 3, '2021-02-22 18:03:22.838553', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (39, '87d095a0c8', 'Paid', 3, '2021-02-22 18:05:32.056189', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (40, 'fc3a1faeb9', 'Paid', 3, '2021-02-22 18:06:41.898371', '{"13": {"color": "red", "colors": "red", "discount": 10, "image": "21d278cd3fcbd593c7df.jpeg", "name": "Galaxy", "price": 400.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (41, 'f1ab023c7c', 'Paid', 3, '2021-02-22 18:08:40.472804', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (42, 'a7181525ce', 'Paid', 3, '2021-02-22 18:19:33.470584', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (43, '23e9810f4c', 'Paid', 3, '2021-02-22 18:21:44.447323', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (44, '9f1227ce2c', 'Paid', 3, '2021-02-22 18:22:38.166985', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (45, 'b047ba3bdb', 'Paid', 3, '2021-02-22 18:23:28.878882', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (46, 'b1aaf08bff', 'Paid', 3, '2021-02-22 18:29:57.084174', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (47, '2cc2db8af1', 'Paid', 3, '2021-02-22 18:32:01.453208', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (48, '65194d7c90', 'Paid', 3, '2021-02-22 18:33:52.973767', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (49, '9476b9de7d', 'Paid', 3, '2021-02-22 18:36:57.853245', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (50, '9883bfc5c2', 'Paid', 3, '2021-02-22 18:37:36.195343', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (51, '11547029ec', 'Paid', 3, '2021-02-22 18:39:14.975901', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (52, '0ebede258d', 'Paid', 3, '2021-02-22 18:40:33.211691', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (53, 'a52068bd22', 'Paid', 3, '2021-02-22 18:41:56.465198', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (54, 'f3d71b5d61', 'Paid', 3, '2021-02-22 18:50:43.301905', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (55, '909230853e', 'Paid', 3, '2021-02-22 18:53:52.823395', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (56, '81ec229409', 'Paid', 3, '2021-02-22 18:54:28.747703', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 2}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (57, '931eb75553', 'Pending', 3, '2021-02-22 18:55:21.715908', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 2}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (58, '896e52afac', 'Paid', 3, '2021-02-22 18:55:32.412471', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 4}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (59, '2e30a409aa', 'Paid', 3, '2021-02-22 19:19:23.164652', '{"1": {"color": "gray", "colors": "gray,white,black,pink", "discount": 0, "image": "492392c9a1d80c65f3c3.jpg", "name": "macbook pro", "price": 1200.99, "quantity": 2}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (60, 'caf906ebd3', 'Paid', 3, '2021-02-22 19:22:32.793379', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (61, '1ca7f012ed', 'Paid', 3, '2021-02-22 19:25:19.262773', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (62, '990235a68d', 'Paid', 3, '2021-02-22 19:29:20.984493', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (63, '134f5d5c0c', 'Paid', 3, '2021-02-22 19:31:42.059522', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (64, '350b73c8c8', 'Paid', 3, '2021-02-22 19:32:41.730395', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 5}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (65, '100ae607a5', 'Pending', 3, '2021-02-22 19:56:36.671368', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (66, 'b6a4461def', 'Paid', 3, '2021-02-22 20:08:42.442274', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (67, 'b12c52aecb', 'Paid', 3, '2021-02-22 20:19:31.189387', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 2}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (68, 'd2d36a0319', 'Paid', 3, '2021-02-22 20:25:18.739528', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 4}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (69, 'dffa523d74', 'Paid', 3, '2021-02-22 20:27:19.733150', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 2}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (70, '6d3775854e', 'Paid', 3, '2021-02-23 01:10:03.698752', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 3}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (71, '94e7f78ee7', 'Paid', 3, '2021-02-23 01:12:37.269517', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (72, 'edd7251c56', 'Paid', 3, '2021-02-23 01:13:24.687813', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 2}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (73, 'e5d5ed9b74', 'Paid', 3, '2021-02-23 01:14:22.969606', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (74, 'd91e89d1aa', 'Paid', 3, '2021-02-23 01:15:31.190913', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');
INSERT INTO customer_order (id, invoice, status, customer_id, date_created, orders) VALUES (75, '36f3040d2e', 'Paid', 3, '2021-02-23 01:17:26.288019', '{"14": {"color": "black", "colors": "black", "discount": 0, "image": "8cfca12051ae41a5221c.jpeg", "name": "Galaxy M1", "price": 500.0, "quantity": 1}}');

-- Table: rating
CREATE TABLE rating (
	id INTEGER NOT NULL,
	sellername VARCHAR(50),
	product VARCHAR(50),
	rating INTEGER,
	PRIMARY KEY (id)
);


-- Table: register
CREATE TABLE register (
	id INTEGER NOT NULL,
	name VARCHAR(50),
	username VARCHAR(50),
	email VARCHAR(50),
	password VARCHAR(200),
	country VARCHAR(50),
	city VARCHAR(50),
	contact VARCHAR(50),
	address VARCHAR(50),
	zipcode VARCHAR(50),
	profile VARCHAR(200),
	date_created DATETIME NOT NULL,
	itemspurchased INTEGER,
	PRIMARY KEY (id),
	UNIQUE (username),
	UNIQUE (email)
);
INSERT INTO register (id, name, username, email, password, country, city, contact, address, zipcode, profile, date_created, itemspurchased) VALUES (1, 'bugti', 'jamal', 'bugti@gmail.com', X'243262243132242F596864784C5066454B4B534879797937424F345A654B4350724D6A41766974363775755778567450523579475955764C2E794169', 'pakistan', 'quetta', '2345325', 'new street', '3468', 'profile.jpg', '2020-04-04 15:29:17.876467', NULL);
INSERT INTO register (id, name, username, email, password, country, city, contact, address, zipcode, profile, date_created, itemspurchased) VALUES (2, 'jamal', 'baloch', 'admin@site.com', X'243262243132247237704B2F3238324C7A6734686E624773387252694F6D6C6F5475594B6A34556843546D55497436334341556958414E4331387575', 'Pakistan', 'Quetta', '2345325', 'new street', '3468', 'profile.jpg', '2020-04-04 16:49:08.912593', NULL);
INSERT INTO register (id, name, username, email, password, country, city, contact, address, zipcode, profile, date_created, itemspurchased) VALUES (3, 'Sukanya Saha', 'sukanyasaha007', 'sukanyasaha007@gmail.com', X'243262243132244238774942466A2E4D6738676530524745716B3376654E673371484F756438507A6F5465654D63546F3438466E36735A68616F7A6D', 'India', 'Howrah', '09038416059', '21 Munshi Zeller Rahim Lane Salkia, ', '711106', 'profile.jpg', '2021-02-20 19:20:45.250073', NULL);
INSERT INTO register (id, name, username, email, password, country, city, contact, address, zipcode, profile, date_created, itemspurchased) VALUES (4, 'Dipa Saha', 'dipasaha', 'dipa.saha5922@gmail.com', X'243262243132244E524F414A6C4C2F7055734A6B2E344E717873472F754D6E4475632F78735451617A525434694E4B3641515231373138726D325553', 'India', 'Howrah', '09830360264', '21, Munshi Zeller Rahim Lane Salkia', '711106', 'profile.jpg', '2021-02-23 04:15:44.225999', NULL);
INSERT INTO register (id, name, username, email, password, country, city, contact, address, zipcode, profile, date_created, itemspurchased) VALUES (9463, 'Namratha MK', 'namratha2403', 'nmk344@gmail.com', '$2b$12$cs/IgvSGOE8FAwnWb.vVVOKs72H/sc7mLjdxHyOR9b1hKKI5nEqQm', 'India', 'Bengaluru', '7209103801', '203, Gangothri Palmgrove, 22 A Main,', '560070', 'profile.jpg', '2021-02-24 01:27:01.733760', NULL);

-- Table: seller_products
CREATE TABLE seller_products (
	id INTEGER NOT NULL,
	name VARCHAR(500) NOT NULL,
	email VARCHAR(500) NOT NULL,
	products VARCHAR(500) NOT NULL,
	PRIMARY KEY (id)
);
INSERT INTO seller_products (id, name, email, products) VALUES (1, 'Dipa Saha', 'dipa.saha5922@gmail.com', 'watch tv phone');
INSERT INTO seller_products (id, name, email, products) VALUES (2, 'Manisha Saha', 'manishasaha504@gmail.com', 'watch tv phone');
INSERT INTO seller_products (id, name, email, products) VALUES (3, 'Sukanya Saha', 'sukanyasaha003@gmail.com', 'watch tv phone');

-- Table: sold_products
CREATE TABLE sold_products (
	id INTEGER NOT NULL,
	name VARCHAR(500) NOT NULL,
	email VARCHAR(500) NOT NULL,
	product VARCHAR(500) NOT NULL,
	quantity_sold INTEGER NOT NULL,
	PRIMARY KEY (id)
);
INSERT INTO sold_products (id, name, email, product, quantity_sold) VALUES (1, 'Sukanya Saha', 'sukanyasaha007@gmail.com', 'Galaxy M1', 13);

-- Table: user
CREATE TABLE user (
	id INTEGER NOT NULL,
	name VARCHAR(50) NOT NULL,
	username VARCHAR(80) NOT NULL,
	email VARCHAR(120) NOT NULL,
	password VARCHAR(180) NOT NULL,
	profile VARCHAR(180) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (username),
	UNIQUE (email)
);
INSERT INTO user (id, name, username, email, password, profile) VALUES (1, 'jamal', 'jamalbaloch', 'baloch@gmail.com', X'243262243132246C74746C4D696E6E365A30724C52636E67717649554F7A454B476A7354514F5936756A4B504C4E746663466F446F574B696B53486D', 'profile.jpg');
INSERT INTO user (id, name, username, email, password, profile) VALUES (2, 'jamal', 'baloch', 'bugti@gmail.com', X'2432622431322436762E2E6937767232394F5762576E442F596441742E326E6A6954386A5579744638704D365A6269504E52576C486A696246684853', 'profile.jpg');
INSERT INTO user (id, name, username, email, password, profile) VALUES (3, 'jamal', 'jamal', 'test@test.com', X'24326224313224492E54424243324D55484F5650635931305555554775384C5659672F765A64513872615577622E6563435747593550752E75663765', 'profile.jpg');
INSERT INTO user (id, name, username, email, password, profile) VALUES (4, 'bugti', 'baloch1', 'admin@site.com', X'2432622431322435644A754242616A65476342365845534C66575239756166535844687469625268556F6D574C73793363476F376A494B4E6C79476D', 'profile.jpg');
INSERT INTO user (id, name, username, email, password, profile) VALUES (5, 'Sukanya Saha', 'sukanyasaha007', 'sukanyasaha007@gmail.com', X'2432622431322439655A764A6E334137446B596B3730685072393036653473316D62445A3164724B5A41452F42467358323269474D4C6F6446445547', 'profile.jpg');
INSERT INTO user (id, name, username, email, password, profile) VALUES (6, 'Dipa Saha', 'dipasaha', 'dipa.saha5922@gmail.com', X'24326224313224476A7257696C63566E666533397371434F704C78732E4B6663627176596E787A4148425A2E4C5644754975754F5930467947327065', 'profile.jpg');
INSERT INTO user (id, name, username, email, password, profile) VALUES (7, 'Manisha Saha', 'manisha', 'manishasaha504@gmail.com', X'2432622431322452426F6F59732E3243376E6D7777656D59414D696D756C6F69614C5445476F4173465A5030334F3173692F63634A315A6571436C71', 'profile.jpg');
INSERT INTO user (id, name, username, email, password, profile) VALUES (8, 'Sukanya Saha', 'sukanyasaha003', 'sukanyasaha003@gmail.com', X'24326224313224584B6F684E7072636D336835346F6B6D4D534569692E3033572F35705848484445734B3134786B71685541374952464E4472636247', 'profile.jpg');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
