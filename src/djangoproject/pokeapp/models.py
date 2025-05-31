from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class PokemonSpecies(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Pokemon species"


class PokemonAbility(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Pokemon abilities"


class PokemonStat(models.Model):
    class PokemonStatName(models.TextChoices):
        HP = "hp"
        ATTACK = "attack"
        DEFENSE = "defense"
        SPECIAL_ATTACK = "special-attack"
        SPECIAL_DEFENSE = "special-defense"
        SPEED = "speed"
        ACCURACY = "accuracy"
        EVASION = "evasion"

    name = models.CharField(max_length=64, choices=PokemonStatName.choices)
    is_battle_only = models.BooleanField()

    def __str__(self):
        return f"{self.name}"


class Pokemon(models.Model):
    pokedex_no = models.IntegerField()
    name = models.CharField(max_length=64)
    types = models.ManyToManyField(PokemonType)
    species = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    abilities = models.ManyToManyField(PokemonAbility)
    weight = models.IntegerField()
    height = models.IntegerField()
    base_experience = models.IntegerField()
    is_default = models.BooleanField()

    def __str__(self):
        return f"{self.name}"


class PokemonStatValue(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    stat = models.ForeignKey(PokemonStat, on_delete=models.CASCADE)
    value = models.IntegerField()


class PokemonForm(models.Model):
    form = models.CharField(max_length=64)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    is_default = models.BooleanField()
