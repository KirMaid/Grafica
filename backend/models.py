from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ReportTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    json_file_path = db.Column(db.String(255), nullable=True)

class VisualizationTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_template_id = db.Column(db.Integer, db.ForeignKey('report_template.id'), nullable=False)
    visualization_type = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
