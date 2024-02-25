from pydantic import BaseModel, Field


class AppBaseModel(BaseModel):
    pass

class AppReponseBaseModel(BaseModel):
    id: str
