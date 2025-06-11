#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from . import std
from .__variants__ import default as base

from gel.models.pydantic import OptionalLink, OptionalProperty



#
# type default::Item
#
class Item(base.Item):
    description: OptionalProperty[std.str, str]
    title: OptionalProperty[std.str, str]
    owner: OptionalLink[User]

#
# type default::User
#
class User(base.User):
    email: OptionalProperty[std.str, str]
    full_name: OptionalProperty[std.str, str]
    identity: OptionalLink[ext_auth.Identity]


from .ext import auth as ext_auth  # noqa: E402 F403

from builtins import str  # noqa: E402 F403


__all__ = (
    'Item',
    'User',
)
