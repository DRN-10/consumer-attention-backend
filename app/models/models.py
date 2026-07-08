from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from uuid import UUID, uuid4

class Role(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str 

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    role_id: UUID = Field(foreign_key="role.id")
    is_active: bool = True

class Store(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    location: str
    metadata_info: Optional[str] = None
    shelves: List["Shelf"] = Relationship(back_populates="store")

class Shelf(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    store_id: UUID = Field(foreign_key="store.id")
    shelf_name: str
    zone_coordinates: str 
    store: Store = Relationship(back_populates="shelves")