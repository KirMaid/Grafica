CREATE DATABASE report_system;
USE report_system;

CREATE TABLE templates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    template_id INT,
    data JSON NOT NULL,
    FOREIGN KEY (template_id) REFERENCES templates(id)
);
