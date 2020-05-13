from dataclasses import dataclass, field
from typing import Optional, List

from .base import BaseModel


@dataclass
class Geo(BaseModel):
    coordinates: Optional[List[float]] = field(default=None, repr=False)
    type: Optional[str] = field(default=None)


@dataclass
class Location(BaseModel):
    """
    A class representing the Geo object.

    Refer: https://developer.twitter.com/en/docs/tweets/enrichments/overview/profile-geo
    """
    country: Optional[str] = field(default=None, repr=False)
    country_code: Optional[str] = field(default=None, repr=False)
    locality: Optional[str] = field(default=None, repr=False)
    region: Optional[str] = field(default=None, repr=False)
    sub_region: Optional[str] = field(default=None, repr=False)
    full_name: Optional[str] = field(default=None)
    geo: Optional[Geo] = field(default=None, repr=False)
