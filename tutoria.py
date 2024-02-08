from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Tutorial(Base):
    __tablename__ = 'tutorials'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    published = Column(Boolean)
    long_description = Column(String(255))
    tutorial_tags = relationship("TutorialTag", back_populates="tutorial")

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    tutorial_tags = relationship("TutorialTag", back_populates="tag")

class TutorialTag(Base):
    __tablename__ = 'tutorial_tags'
    tutorial_id = Column(Integer, ForeignKey('tutorials.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)
    tutorial = relationship("Tutorial", back_populates="tutorial_tags")
    tag = relationship("Tag", back_populates="tutorial_tags")
