from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from dogs.models import Dog, Breed


class DogSerializer(ModelSerializer):
    """
    Сериализатор для создания и обновления экземпляров модели Dog.

    Включает все поля модели Dog.
    """
    class Meta:
        model = Dog
        fields = "__all__"


class DogListSerializer(DogSerializer):
    """
    Сериализатор для отображения списка собак.

    Дополнительно:
        avg_breed_age (Decimal): Средний возраст собак той же породы.
    """
    avg_breed_age = serializers.DecimalField(
        max_digits=3, decimal_places=2, read_only=True
    )


class DogDetailSerializer(DogSerializer):
    """
    Сериализатор для детального представления собаки.

    Дополнительно:
        same_breed_count (int): Количество собак той же породы.
    """
    same_breed_count = serializers.IntegerField(read_only=True)


class BreedSerializer(ModelSerializer):
    """
    Сериализатор для модели Breed.

    Дополнительно:
        dogs_count (int): Количество собак этой породы.
    """
    dogs_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = "__all__"