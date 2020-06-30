from dataclasses import dataclass, field
from typing import Optional

from .base import BaseModel


@dataclass
class Token(BaseModel):
    token_type: Optional[str]
    access_token: Optional[str]
