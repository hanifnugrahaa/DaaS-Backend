# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
# Nanti kalo pake Psql, URL-nya kayak gini:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host/dbname"

# Engine ini adalah 'jantung' koneksi.
# connect_args itu khusus buat SQLite biar aman di-handle multi-thread
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Ini adalah 'kasir' yang bakal ngelayanin tiap request ke DB.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Bikin 'cetakan' dasar yang bakal dipake sama semua model tabel (Users, Subscriptions) nanti.
Base = declarative_base