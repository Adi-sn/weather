from pydantic import BaseModel
from typing import List

#Gemini Payload
class Text(BaseModel):
    text:str
class Parts(BaseModel):
    parts:List[Text]
class Content(BaseModel):
    contents:List[Parts]