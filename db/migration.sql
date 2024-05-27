CREATE TABLE report_template (
    id INTEGER PRIMARY KEY,
    name VARCHAR(80) UNIQUE NOT NULL,
    content TEXT NOT NULL,
    json_file_path VARCHAR(255),
    FOREIGN KEY (id) REFERENCES report_visualization(report_template_id)
);

CREATE TABLE visualization_template (
    id INTEGER PRIMARY KEY,
    visualization_type VARCHAR(64) UNIQUE NOT NULL,
    FOREIGN KEY (id) REFERENCES report_visualization(visualization_template_id)
);

CREATE TABLE report_visualization (
    report_template_id INTEGER,
    visualization_template_id INTEGER,
    PRIMARY KEY (report_template_id, visualization_template_id),
    FOREIGN KEY (report_template_id) REFERENCES report_template(id),
    FOREIGN KEY (visualization_template_id) REFERENCES visualization_template(id)
);

