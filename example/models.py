from django.db import models


class Korisnik(models.Model):
    ime = models.CharField(max_length=30)
    email = models.CharField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)


class Aktivnost(models.Model):
    naziv = models.CharField(max_length=30)
    zanr = models.CharField(max_length=30)
    ocena = models.IntegerField()
    godinaIzdanja = models.IntegerField()


class Muzika(Aktivnost):
    izvodjac = models.CharField(max_length=30)


class Knjiga(Aktivnost):
    pisac = models.CharField(max_length=30)


class Film(Aktivnost):
    reziser = models.CharField(max_length=30)