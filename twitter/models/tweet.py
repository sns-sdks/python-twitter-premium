from dataclasses import dataclass, field
from typing import Optional, List, Dict

from .base import BaseModel
from .user import User
from .place import Coordinates, Place
from .entities import Entities, ExtendedEntities


@dataclass
class Rule(BaseModel):
    """
    A class representing rule object.

    Refer: https://developer.twitter.com/en/docs/tweets/enrichments/overview/matching-rules
    """

    tag: Optional[str] = field(default=None)
    id: Optional[int] = field(default=None, repr=False)
    id_str: Optional[str] = field(default=None, repr=False)


@dataclass
class CurrentUserRetweet(BaseModel):
    id: Optional[int] = field(default=None, repr=False)
    id_str: Optional[str] = field(default=None, repr=False)


@dataclass
class QuotedStatusPermalink(BaseModel):
    """
    A class representing new object for quoted_status_permalink.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json
    """

    url: Optional[str] = field(default=None)
    expanded: Optional[str] = field(default=None, repr=False)
    display: Optional[str] = field(default=None, repr=False)


@dataclass
class Tweet(BaseModel):
    """
    A class representing tweet object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
    """

    created_at: Optional[str] = field(default=None)
    id: Optional[int] = field(default=None, repr=False)
    id_str: Optional[str] = field(default=None)
    text: Optional[str] = field(default=None, repr=False, compare=False)
    source: Optional[str] = field(default=None, repr=False, compare=False)
    truncated: Optional[bool] = field(default=None, repr=False, compare=False)
    in_reply_to_status_id: Optional[int] = field(default=None, repr=False, compare=False)
    in_reply_to_status_id_str: Optional[str] = field(default=None, repr=False, compare=False)
    in_reply_to_user_id: Optional[int] = field(default=None, repr=False, compare=False)
    in_reply_to_user_id_str: Optional[str] = field(default=None, repr=False, compare=False)
    in_reply_to_screen_name: Optional[str] = field(default=None, repr=False, compare=False)
    user: Optional[User] = field(default=None, repr=False, compare=False)
    full_text: Optional[str] = field(default=None, repr=False, compare=False)
    display_text_range: Optional[List[int]] = field(default=None, repr=False, compare=False)
    coordinates: Optional[Coordinates] = field(default=None, repr=False, compare=False)
    place: Optional[Place] = field(default=None, repr=False, compare=False)
    quoted_status_id: Optional[int] = field(default=None, repr=False, compare=False)
    quoted_status_id_str: Optional[int] = field(default=None, repr=False, compare=False)
    is_quote_status: Optional[int] = field(default=None, repr=False, compare=False)
    extended_tweet: Optional["Tweet"] = field(default=None, repr=False, compare=False)
    quoted_status: Optional["Tweet"] = field(default=None, repr=False, compare=False)
    quoted_status_permalink: Optional[QuotedStatusPermalink] = field(default=None, repr=False, compare=False)
    retweeted_status: Optional["Tweet"] = field(default=None, repr=False, compare=False)
    quote_count: Optional[int] = field(default=None, repr=False, compare=False)
    reply_count: Optional[int] = field(default=None, repr=False, compare=False)
    retweet_count: Optional[int] = field(default=None, repr=False, compare=False)
    favorite_count: Optional[int] = field(default=None, repr=False, compare=False)
    entities: Optional[Entities] = field(default=None, repr=False, compare=False)
    extended_entities: Optional[ExtendedEntities] = field(default=None, repr=False, compare=False)
    favorited: Optional[bool] = field(default=None, repr=False, compare=False)
    retweeted: Optional[bool] = field(default=None, repr=False, compare=False)
    possibly_sensitive: Optional[bool] = field(default=None, repr=False, compare=False)
    filter_level: Optional[str] = field(default=None, repr=False, compare=False)
    lang: Optional[str] = field(default=None, repr=False, compare=False)
    matching_rules: Optional[List[Rule]] = field(default=None, repr=False, compare=False)
    current_user_retweet: Optional[CurrentUserRetweet] = field(default=None, repr=False, compare=False)
    scopes: Optional[Dict[str, bool]] = field(default=None, repr=False, compare=False)
    withheld_copyright: Optional[bool] = field(default=None, repr=False, compare=False)
    withheld_in_countries: Optional[List[str]] = field(default=None, repr=False, compare=False)
    withheld_scope: Optional[str] = field(default=None, repr=False, compare=False)
