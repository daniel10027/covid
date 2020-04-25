from django.db import models
from tinymce import HTMLField

# Create your models here.
class Pays(models.Model):
    """Model definition for Pays."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50)
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    class Meta:
        """Meta definition for Pays."""

        verbose_name = 'Pays'
        verbose_name_plural = 'Pays'

    def __str__(self):
        """Unicode representation of Pays."""
        return self.nom

    def get_absolute_url(self):

        return reverse("site-home", kwargs={"pk": self.pk}) # rediriger apres creation de produuits

class Localite(models.Model):
    """Model definition for Localite."""

    # TODO: Define fields here
    nom         = models.CharField( max_length=50,help_text= 'Nom dela localite')
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, related_name="localite_pays")
    cas_declare = models.IntegerField()
    cas_confirme = models.IntegerField()
    nombre_deces = models.IntegerField()
    gueri = models.IntegerField()
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Localite."""

        verbose_name = 'Localite'
        verbose_name_plural = 'Localites'

    def __str__(self):
        """Unicode representation of Localite."""
        return self.nom

    

    def get_absolute_url(self):
        """Return absolute url for Localite."""
        pass
        

    # TODO: Define custom methods here

class Conseil(models.Model):
    """Model definition for Conseil."""

    # TODO: Define fields here
    description         = HTMLField('Description')
    status      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Conseil."""

        verbose_name = 'Conseil'
        verbose_name_plural = 'Conseils'

    def __str__(self):
        """Unicode representation of Conseil."""
        return self.nom



    def get_absolute_url(self):
        """Return absolute url for Conseil."""
        return ('')

    # TODO: Define custom methods here
