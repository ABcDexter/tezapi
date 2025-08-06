#################
#    Imports    #
#################
from sqlmodel import SQLModel, Field
from typing import Optional

#################
#    Classes    #   
#################


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)      # Optional makes it nullable before insertion
    name: str = Field(min_length=3, max_length=15, index=True)     # Name must be between 3 and 15 characters long
    description: Optional[str] = Field(default=None, max_length=255)  # Description is optional and can be up to 255 characters long