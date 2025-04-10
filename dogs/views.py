from django.db.models import Avg, Count, Subquery, OuterRef
from rest_framework.viewsets import ModelViewSet
from dogs.models import Dog, Breed
from dogs.serializers import (
    DogListSerializer,
    DogDetailSerializer,
    BreedSerializer,
    DogSerializer,
)


class DogViewSet(ModelViewSet):
    """
        ViewSet для модели Dog.

        Поддерживает стандартные CRUD-операции.
        Добавляет:
            - Средний возраст собак той же породы в списке.
            - Количество собак той же породы в детальном представлении.
        """
    queryset = Dog.objects.all()

    def get_queryset(self):
        """
        Возвращает queryset с аннотациями в зависимости от действия.

        Возвращает:
            QuerySet: Аннотированный набор объектов Dog.
        """
        if self.action == "list":
            return Dog.objects.all().annotate(
                avg_breed_age=Subquery(
                    Dog.objects.filter(breed=OuterRef("breed"))
                    .values("breed")
                    .annotate(avg_age=Avg("age"))
                    .values("avg_age")
                )
            )
        elif self.action == "retrieve":
            return Dog.objects.all().annotate(
                same_breed_count=Count("breed__dogs"),
            )
        return super().get_queryset()

    def get_serializer_class(self):
        """
        Возвращает соответствующий класс сериализатора в зависимости от действия.

        Возвращает:
            Serializer: Класс сериализатора для текущего действия.
        """
        if self.action == "list":
            return DogListSerializer
        elif self.action == "retrieve":
            return DogDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return DogSerializer
        return super().get_serializer_class()


class BreedViewSet(ModelViewSet):
    """
    ViewSet для модели Breed.

    Поддерживает стандартные CRUD-операции.
    Включает аннотацию количества собак в списке пород.
    """
    queryset = Breed.objects.all().annotate(dogs_count=Count("dogs"))
    serializer_class = BreedSerializer