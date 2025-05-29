from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class PokemonSpecies(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class Pokemon(models.Model):
    pokedex_no = models.IntegerField()
    name = models.CharField(max_length=64)
    types = models.ManyToManyField(PokemonType)
    species = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
