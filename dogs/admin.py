from django.contrib import admin
from dogs.models import Dog, Breed


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
        "favorite_toy",
    )
    list_filter = ("breed", "gender", "color")
    search_fields = ("name", "breed__name")


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_needs",
    )
    list_filter = ("size",)
    search_fields = ("name",