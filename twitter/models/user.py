"""
    User object
"""
from dataclasses import dataclass, field
from typing import List, Optional

from .base import BaseModel
from .geo import Location
from .entities import UserEntities


@dataclass
class Derived(BaseModel):
    """
    A class representing User extend deride objects
    """

    locations: Optional[List[Location]] = field(default=None)


@dataclass
class User(BaseModel):
    """
    A class representing the user object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object
    """

    id: Optional[int] = field(default=None, repr=False)
    id_str: Optional[str] = field(default=None, repr=False)
    name: Optional[str] = field(default=None, repr=False)
    screen_name: Optional[str] = field(default=None, repr=False)
    protected: Optional[bool] = field(default=None, repr=False, compare=False)
    verified: Optional[bool] = field(default=None, repr=False, compare=False)
    followers_count: Optional[int] = field(default=None, repr=False, compare=False)
    friends_count: Optional[int] = field(default=None, repr=False, compare=False)
    listed_count: Optional[int] = field(default=None, repr=False, compare=False)
    favourites_count: Optional[int] = field(default=None, repr=False, compare=False)
    statuses_count: Optional[int] = field(default=None, repr=False, compare=False)
    created_at: Optional[str] = field(default=None, repr=False, compare=False)
    profile_banner_url: Optional[str] = field(default=None, repr=False, compare=False)
    profile_image_url_https: Optional[str] = field(default=None, repr=False, compare=False)
    default_profile: Optional[bool] = field(default=None, repr=False, compare=False)
    default_profile_image: Optional[bool] = field(default=None, repr=False, compare=False)
    location: Optional[str] = field(default=None, repr=False, compare=False)
    derived: Optional[Derived] = field(default=None, repr=False, compare=False)
    url: Optional[str] = field(default=None, repr=False, compare=False)
    description: Optional[str] = field(default=None, repr=False, compare=False)
    withheld_in_countries: Optional[List[str]] = field(default=None, repr=False, compare=False)
    withheld_scope: Optional[str] = field(default=None, repr=False, compare=False)
    entities: Optional[UserEntities] = field(default=None, repr=False, compare=False)
