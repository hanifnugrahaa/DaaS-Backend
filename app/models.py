from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # 'subscriptions' bakal jadi list subscription punya user ini
    subscriptions = relationship("Subscription", back_populates="owner")
    api_keys = relationship("ApiKey", back_populates="owner")

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    # Ini 'plan_name' pake Enum biar datanya 'bersih', gabisa diisi ngawur.
    plan_name = Column(SQLEnum(['basic', 'premium', 'enterprise'], name="plan_types"), nullable=False)
    start_date = Column(DateTime(timezone=True), server_default=func.now())
    end_date = Column(DateTime(timezone=True), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id")) # Foreign Key ke tabel 'users'

    # 'owner' adalah User yang punya subscription ini
    owner = relationship(User, back_populates="subscriptions")

class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    # simpen HASH-nya, bukan key aslinya. Biar aman.
    hashed_key = Column(String, unique=True, index=True, nullable=False)
    status = Column(SQLEnum(['active', 'revoked'], name="key_status"), default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_used_at = Column(DateTime(timezone=True), nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship(User, back_populates="api_keys")