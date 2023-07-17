#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""
