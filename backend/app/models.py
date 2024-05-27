from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

report_visualization_association = Base.metadata.create_table(
    'report_visualization',
    Column('report_template_id', Integer, ForeignKey('report_template.id')),
    Column('visualization_template_id', Integer, ForeignKey('visualization_template.id'))
)

class ReportTemplate(Base):
    __tablename__ = 'report_template'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    content = Column(Text, nullable=False)
    json_file_path = Column(String(255), nullable=True)
    visualizations = relationship("VisualizationTemplate", secondary=report_visualization_association, back_populates="reports")

class VisualizationTemplate(Base):
    __tablename__ = 'visualization_template'
    id = Column(Integer, primary_key=True)
    visualization_type = Column(String(64), index=True, unique=True, nullable=False)
    reports = relationship("ReportTemplate", secondary=report_visualization_association, back_populates="visualizations")
