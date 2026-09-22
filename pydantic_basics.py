"""{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "string"
  }
}
"""
import uuid
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class CourseSchema(BaseModel):
    # Если в API все поля приходят в camelCase - Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))  # НО! Явно переданные значения имеют приоритет над дефолтными
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")

# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week"
)

print('Course default model:', course_default_model)

# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)

# Когда мы вызываем response.json(), мы получаем словарь, который можно передать в Pydantic-модель так:
# GetUserResponse(**response.json())

# Инициализируем модель CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)

# Если у нас есть JSON-файл, мы можем загрузить его в Pydantic-модель так:
# import json
# with open("course.json", "r") as file:
#     course_data = file.read()
# course_model = CourseSchema.model_validate_json(course_data)
# print(course_model)

# Когда мы сериализуем Pydantic-модель обратно в JSON (dict() или json()),
# Pydantic по умолчанию сохраняет Python-стиль именования (snake_case).
print(course_dict_model.model_dump())

# Но если нам нужно вернуть JSON в camelCase, то можно использовать by_alias=True:
print(course_dict_model.model_dump(by_alias=True))
print(course_dict_model.model_dump_json(by_alias=True))

# Создадим несколько объектов модели
course1 = CourseSchema()
course2 = CourseSchema()

print(course1.id)
print(course2.id)