from app.core import models as base_model


class Center(base_model.AppBaseModel):
    name: str

    class Config:
        allow_populate_by_field_name = True


class CenterResponse(Center, base_model.AppReponseBaseModel):
    pass