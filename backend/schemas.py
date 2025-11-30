from pydantic import BaseModel
from typing import Optional, List, Dict

class MenuItemSchema(BaseModel):
  id: Optional[int] = None
  name: Dict[str, str]
  description: Optional[Dict[str, str]] = None
  weight: Optional[List[Dict[str, str]]] = None
  price: float
  image: Optional[str] = None

  class Config:
    orm_mode = True
