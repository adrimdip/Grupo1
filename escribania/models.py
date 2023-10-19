from django.db import models
from django.urls import reverse

class ActoJuridico(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        ordering = ['nombre']

    def get_absolute_url(self):
        return reverse("act-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} - {}'.format(self.pk, self.nombre)

class Escribano(models.Model):
    escribano = models.CharField(max_length=150)
    actos_juridicos = models.ManyToManyField(ActoJuridico, related_name="escribanos", blank=True)

    class Meta:
        ordering = ['escribano']

    def get_absolute_url(self):
        return reverse("clerk-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} - {}'.format(self.pk, self.escribano)

class Escritura(models.Model):
    fecha = models.DateField(verbose_name="Fecha de Escritura")
    escribano = models.ForeignKey(Escribano, on_delete=models.CASCADE, null=True, blank=True)
    folio = models.SmallIntegerField(null=True, blank=True)
    acto = models.ForeignKey(ActoJuridico, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Acto Jurídico")
    otorgante = models.CharField(max_length=300)
    aceptante = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse("document-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.fecha, self.aceptante)
