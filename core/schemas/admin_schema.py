from pydantic import BaseModel


class AddRemovePermSchema(BaseModel):
    permission_id: int
    role: int