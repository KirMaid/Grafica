class VisualizationTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_template_id = db.Column(db.Integer, db.ForeignKey('report_template.id'), nullable=False)
    visualization_type = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)

