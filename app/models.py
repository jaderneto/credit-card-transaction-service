# Estruturas (schemas) que descrevem como os dados devem ser recebidos, validados e retornados pela API
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime, UTC


class Card(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    number: str
    name: str
    exp_month: int
    exp_year: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))





