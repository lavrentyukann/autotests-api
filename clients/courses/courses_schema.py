from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Описание структуры курса
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)

    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema
    estimated_time: str
    created_by_user: UserSchema

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, serialize_by_alias=True)

    user_id: str

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, serialize_by_alias=True)

    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)
    preview_file_id: str = Field(default_factory=fake.uuid4)    # только для негативных сценариев,
    created_by_user_id: str = Field(default_factory=fake.uuid4) # для положительных - при инициализации явно указать эти два параметра

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса
    """
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, serialize_by_alias=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)