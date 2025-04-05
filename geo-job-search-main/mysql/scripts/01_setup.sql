use template_db;

CREATE TABLE IF NOT EXISTS jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    company VARCHAR(255),
    summary TEXT,
    link TEXT,
    salary VARCHAR(255)
);