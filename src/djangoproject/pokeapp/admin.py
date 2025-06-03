from django.contrib import admin
from pokeapp.models import (
    Pokemon,
    PokemonAbility,
    PokemonAbilityValue,
    PokemonEvolutionChain,
    PokemonForm,
    PokemonSpecies,
    PokemonStat,
    PokemonStatValue,
    PokemonType,
)


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
        "pokedex_no",
        "name",
        "species",
        "weight",
        "height",
        "base_experience",
        "is_default",
    ]
    list_filter = ["types"]
    filter_horizontal = ("types", "abilities")


class PokemonAbilityAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "name",
    ]


class PokemonFormAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "form",
        "pokemon",
        "is_default",
    ]
    list_filter = ["pokemon", "is_default"]


class PokemonStatAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = ["id", "name", "is_battle_only"]


class PokemonStatValueAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "pokemon",
        "stat",
        "value",
    ]


class PokemonAbilityValueAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "pokemon",
        "ability",
        "is_hidden",
    ]


class PokemonEvolutionChainAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "species",
        "unevolved",
        "first_evolution",
        "second_evolution",
    ]


admin.site.register(PokemonType, PokemonTypeAdmin)
admin.site.register(PokemonSpecies, PokemonSpeciesAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonForm, PokemonFormAdmin)
admin.site.register(PokemonStat, PokemonStatAdmin)
admin.site.register(PokemonStatValue, PokemonStatValueAdmin)
admin.site.register(PokemonAbility, PokemonAbilityAdmin)
admin.site.register(PokemonAbilityValue, PokemonAbilityValueAdmin)
admin.site.register(PokemonEvolutionChain, PokemonEvolutionChainAdmin)
