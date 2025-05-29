from django.contrib import admin

from api.models import Pokemon, PokemonSpecies, PokemonType


class PokemonTypeAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "name",
    ]


class PokemonSpeciesAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "name",
    ]


class PokemonAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "name",
        "pokedex_no",
        "species",
        "weight",
    ]
    list_filter = ["species"]
    filter_horizontal = ("types",)


admin.site.register(PokemonType, PokemonTypeAdmin)
admin.site.register(PokemonSpecies, PokemonSpeciesAdmin)
admin.site.register(Pokemon, PokemonAdmin)
