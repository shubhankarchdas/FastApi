from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from uuid import uuid4
from typing import Union

class Book(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), alias="_id")
    title: str
    author: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

    # ✅ Updated for Pydantic v2
    model_config = ConfigDict(
        validate_by_name=True,
        json_schema_extra={
            "example": {
                "title": "The Pragmatic Programmer",
                "author": "Andrew Hunt",
                "description": "A book about software craftsmanship.",
                "price": 29.99,
                "in_stock": True
            }
        }
    )



class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None

