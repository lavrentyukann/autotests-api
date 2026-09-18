from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class Exercise(TypedDict):
    """
    Описание структуры задания
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания задания
    """
    exercise: Exercise

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий
    """
    courseId: str

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения заданий
    """
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения задания
    """
    exercise: Exercise

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа изменения задания
    """
    exercise: Exercise

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # метод создает задание, возвращает объект
    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Создаёт задание и возвращает распарсенный JSON-ответ.

        :param request: Словарь с данными задания (title, courseId, maxScore, minScore, orderIndex, description, estimatedTime).
        :return: Словарь с созданным заданием: { "exercise": Exercise }.
        """
        response = self.create_exercise_api(request)
        return response.json()

    #
    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получает список заданий курса и возвращает распарсенный JSON-ответ.

        :param query: Словарь с courseId для фильтрации.
        :return: Словарь со списком заданий: { "exercises": list[Exercise] }.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Получает задание по ID и возвращает распарсенный JSON-ответ.

        :param exercise_id: Идентификатор задания.
        :return: Словарь с заданием: { "exercise": Exercise }.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Частично обновляет задание и возвращает распарсенный JSON-ответ.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с полями для обновления (все Optional).
        :return: Словарь с обновлённым заданием: { "exercise": Exercise }.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))