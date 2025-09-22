import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Pregunta(models.Model):
    texto_pregunta = models.CharField(
        max_length=200,
        verbose_name=_("Ingresa pregunta")
    )
    fecha_publicacion = models.DateTimeField(_("Fecha de publicación"))

    class Meta:
        verbose_name = _("Pregunta")
        verbose_name_plural = _("Preguntas")

    def __str__(self):
        return self.texto_pregunta

    def fue_publicada_recientemente(self):
        """Retorna True si la pregunta se publicó en las últimas 24 horas"""
        return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=1)


class Opcion(models.Model):
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        verbose_name=_("Pregunta")
    )
    texto_opcion = models.CharField(
        max_length=200,
        verbose_name=_("Texto de opción")
    )
    votos = models.IntegerField(default=0, verbose_name=_("Votos"))

    class Meta:
        verbose_name = _("Opción")
        verbose_name_plural = _("Opciones")

    def __str__(self):
        return self.texto_opcion
