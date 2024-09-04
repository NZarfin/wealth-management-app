-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Create clients table
CREATE TABLE IF NOT EXISTS clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    type ENUM('credit', 'debit') NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Insert initial data into users table
INSERT INTO users (username, password_hash, email) VALUES
('admin', '$2b$12$KIXQmQnEnWwZT9wDF6B6O.y5m.E1xDFnBh/Pc9n8tK03/k.Zdc3t2', 'admin@example.com');

-- Insert initial data into clients table
INSERT INTO clients (name, email, user_id) VALUES
('John Doe', 'john@example.com', 1);

-- Insert initial data into transactions table
INSERT INTO transactions (client_id, date, amount, type) VALUES
(1, '2024-01-01', 500.00, 'credit'),
(1, '2024-01-02', 200.00, 'debit');
