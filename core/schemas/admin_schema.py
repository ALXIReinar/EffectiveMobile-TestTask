from pydantic import BaseModel


class AddRemovePermSchema(BaseModel):
    permission_id: int
    role: int


class CreateActionSchema(BaseModel):
    name: str
    description: str


class UpdateActionSchema(BaseModel):
    name: str
    description: str


class CreateServiceSchema(BaseModel):
    name: str
    description: str


class UpdateServiceSchema(BaseModel):
    name: str
    description: str


class CreatePermissionSchema(BaseModel):
    service_id: int
    action_id: int
    description: str


class UpdatePermissionSchema(BaseModel):
    description: str


class CreateRoleSchema(BaseModel):
    name: str
    description: str


class UpdateRoleSchema(BaseModel):
    name: str
    description: str