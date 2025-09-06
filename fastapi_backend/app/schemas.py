import uuid

from fastapi_users import schemas
from pydantic import BaseModel
from uuid import UUID


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class ItemBase(BaseModel):
    name: str
    description: str | None = None
    quantity: int | None = None


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: UUID
    user_id: UUID

    model_config = {"from_attributes": True}


class Claim(BaseModel):
    diagnosis: str
    code: str

    def validate_gcc(self):
        valid_codes = {"E11.9", "I10", "S52.5"}  # Sample ICD-10 for GCC
        if self.code not in valid_codes:
            raise ValueError("Invalid GCC-compliant code")
        return True
