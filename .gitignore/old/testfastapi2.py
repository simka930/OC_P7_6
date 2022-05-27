from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Blog(BaseModel):
    title: str
    body:  str
    published:Optional[bool]




@app.post('/blog')
def create(request: Blog):
    return request




#%%
