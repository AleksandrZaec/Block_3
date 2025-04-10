from django.db import models


class Breed(models.Model):
    """
    Представляет породу собаки.

    Атрибуты:
        name (str): Название породы.
        size (str): Размер породы (Tiny, Small, Medium, Large).
        friendliness (int): Уровень дружелюбия от 1 до 5.
        trainability (int): Обучаемость от 1 до 5.
        shedding_amount (int): Уровень линьки от 1 до 5.
        exercise_needs (int): Потребность в физических нагрузках от 1 до 5.
    """
    SIZE_CHOICES = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]
    INT_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=INT_CHOICES)
    trainability = models.IntegerField(choices=INT_CHOICES)
    shedding_amount = models.IntegerField(choices=INT_CHOICES)
    exercise_needs = models.IntegerField(choices=INT_CHOICES)

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    """
    Представляет конкретную собаку.

    Атрибуты:
        name (str): Имя собаки.
        age (int): Возраст собаки в годах.
        breed (Breed): Внешний ключ к породе.
        gender (str): Пол собаки ('Male' или 'Female').
        color (str): Окрас собаки.
        favorite_food (str): Любимая еда собаки.
        favorite_toy (str): Любимая игрушка собаки.
    """
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    breed = models.ForeignKey(
        Breed, on_delete=models.SET_NULL, related_name="dogs", default=None, null=True
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
