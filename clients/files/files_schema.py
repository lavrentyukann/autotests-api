from pydantic import BaseModel, HttpUrl, ConfigDict
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    """
    Описание структуры файла
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, serialize_by_alias=True)

    filename: str
    directory: str
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла
    """
    file: FileSchema
