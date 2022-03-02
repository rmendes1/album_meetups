from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.name} ({self.address})'

class Participant(models.Model):
    email = models.EmailField(unique = True)
    

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length = 200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null = True) # null won't have effects in MtM relationships
    #without null = True, if you have blank = True, for some fields (like CharField), default empty values (e.g. empty strings) would be stored - others would cause an error


    def __str__(self):
        return self.title