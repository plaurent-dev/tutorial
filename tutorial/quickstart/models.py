from django.db import models


# Create your models here.
class Regex(models.Model):

    class Meta:
        managed = True
        app_label = 'tutorial'

    key = models.CharField(unique=True, max_length=255)
    value = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

    def __str__(self):
        return '%s: %s' % (self.key, self.value)


# Create your models here.
class Const(models.Model):

    class Meta:
        managed = True
        app_label = 'tutorial'

    key = models.CharField(unique=True, max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return '%s: %s' % (self.key, self.value)

# Create your models here.
class Constants(models.Model):

    class Meta:
        managed = True
        app_label = 'tutorial'

    key = models.CharField(unique=True, max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return '%s: %s' % (self.key, self.value)

# Create your models here.
class App(models.Model):

    class Meta:
        managed = True
        app_label = 'tutorial'

    appname = models.CharField(unique=True, max_length=255)
    appversion = models.CharField(max_length=255)
    appcontent = models.TextField()
    appcreated_on = models.DateTimeField(auto_now_add=True)
    regex = models.ManyToManyField(Regex)
    constructeur = models.ForeignKey(Const, on_delete=models.DO_NOTHING)
    constants  = models.ManyToManyField(Constants)
