from django.contrib import admin

from api.models import Pokemon, PokemonForm, PokemonSpecies, PokemonStat, PokemonStatValue, PokemonType


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
    filter_horizontal = ("types", )


class PokemonFormAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "pokemon",
        "name",
        "form_name",
        "is_default",
    ]
    list_filter = ["pokemon"]


class PokemonStatAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "name",
        "is_battle_only"
    ]


class PokemonStatValueAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "stat",
        "value"
    ]


admin.site.register(PokemonType, PokemonTypeAdmin)
admin.site.register(PokemonSpecies, PokemonSpeciesAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonForm, PokemonFormAdmin)
admin.site.register(PokemonStat, PokemonStatAdmin)
admin.site.register(PokemonStatValue, PokemonStatValueAdmin)
