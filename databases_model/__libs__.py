from sqlalchemy import create_engine, ForeignKey, Column, Row, Integer, CHAR, String, DATETIME, DateTime
from sqlalchemy.orm import sessionmaker, relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import INTEGER
from create_app import Base
