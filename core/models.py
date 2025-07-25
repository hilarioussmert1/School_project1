from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     ROLE_CHOICES = [
#         ('admin', 'Admin'),
#         ('coach', 'Coach'),
#         ('player', 'Player'),
#         ('referee', 'Referee'),
#         ('owner', 'Owner'),
#     ]
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='player')


# Model representing a division (group) of teams
class Division(models.Model):
    division = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.division}"  # Returns division name as string


# Model representing a team
class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    group = models.ForeignKey(Division, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()

    # Validation logic for the Team model
    def clean(self):
        # City must not be empty
        if not self.city.strip():
            raise ValidationError({'city': 'City cannot be empty.'})

        # Name must not be empty
        if not self.name.strip():
            raise ValidationError({'name': 'Name cannot be empty.'})

        # City must contain only alphabetic characters
        if not self.city.replace(" ", "").isalpha():
            raise ValidationError({'city': 'City must contain only letters.'})

        # Name must contain only alphabetic characters
        if not self.name.replace(" ", "").isalpha():
            raise ValidationError({'name': 'Name must contain only letters.'})

    def __str__(self):
        return f"{self.name}"  # Returns the team's name as string


# Abstract base class for people (used for inheritance)
class Person(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    # If the associated team is deleted, this will be set to NULL

    class Meta:
        abstract = True  # This model won't create a database table


# Player model inheriting from Person
class Player(Person):
    playingToday = models.BooleanField(default=False)  # Indicates if the player is active today
    number = models.PositiveIntegerField()  # Player's jersey number

    def clean(self):
        # Number must be between 1 and 99
        if not (1 <= self.number <= 99):
            raise ValidationError("The number has to be between 1 and 99")

    def __str__(self):
        # Returns formatted player information
        return f"{self.number} | {self.firstName} {self.lastName} | {self.team}"


# Model representing team statistics
class Statistic(models.Model):
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    gamesPlayed = models.PositiveIntegerField()
    goals = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    losses = models.PositiveIntegerField()
    draws = models.PositiveIntegerField()
    points = models.PositiveIntegerField()

    def __str__(self):
        return str(self.team)  # Returns team name associated with this statistic


# Model representing a club
class Club(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  # Unique identifier for URLs
    description = models.TextField()
    founded = models.IntegerField(null=True, blank=True)  # Year of founding

    def clean(self):
        # Ensure club name is unique (case-insensitive)
        if Club.objects.filter(name__iexact=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'A club with this name already exists.'})

    def __str__(self):
        return self.name  # Returns the club name as string


# Model representing news or announcements
class News(models.Model):
    title = models.CharField(max_length=200)  # Title of the news
    info = models.TextField()  # Full news content
    date = models.DateTimeField(default=timezone.now)  # Date and time of publication

    def clean(self):
        # News date cannot be in the past
        if self.date < timezone.now():
            raise ValidationError({'date': 'Date cannot be in the past.'})

    def __str__(self):
        return self.title  # Returns the news title






    #1. сделать validation for [type check] [existance check]
    #2. Binary search - done
    #3. OWN sort - done



















