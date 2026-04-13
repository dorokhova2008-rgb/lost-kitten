CREATE TABLE roles (
    id_role INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE users (
    id_user INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role_id INT NOT NULL REFERENCES roles(id_role)
);

CREATE TABLE categories (
    id_category INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    category_description VARCHAR(300)
);

CREATE TABLE products (
    id_product INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    product_description VARCHAR(500),
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    category_id INT NOT NULL REFERENCES categories(id_category)
);

CREATE TABLE carts (
    id_cart INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INT NOT NULL UNIQUE REFERENCES users(id_user)
);

CREATE TABLE cart_items (
    id_cart_item INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cart_id INT NOT NULL REFERENCES carts(id_cart),
    product_id INT NOT NULL REFERENCES products(id_product),
    item_quantity INT NOT NULL CHECK (item_quantity > 0)
);

CREATE TABLE orders (
    id_order INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id_user),
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    order_status VARCHAR(50) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL CHECK (total_amount > 0)
);

CREATE TABLE order_items (
    id_order_item INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id INT NOT NULL REFERENCES orders(id_order),
    product_id INT NOT NULL REFERENCES products(id_product),
    orderitems_quantity INT NOT NULL CHECK (orderitems_quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL CHECK (unit_price > 0)
);