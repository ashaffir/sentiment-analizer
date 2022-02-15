""" 
Communicating with Opensea
--------------------------
- Get collections per owner
- Get statistics on particular collection
- Get assets per particular collection

"""

from pydantic import BaseModel
from typing import Optional


class Collection(BaseModel):
    owner: str
    name: str
    address: str
    slug: str
    tracked: Optional[bool] = False


class Owner(BaseModel):
    """Collection Owner

    Args:
        BaseModel ([type]): [description]
    """

    name: str
    address: str
