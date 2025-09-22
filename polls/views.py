from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Pregunta, Opcion
from .forms import PreguntaForm, OpcionForm

# Lista de preguntas recientes
class VistaIndice(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "lista_preguntas"

    def get_queryset(self):
        """Retorna las 5 preguntas más recientes"""
        return Pregunta.objects.order_by("-fecha_publicacion")[:5]

# Detalle de la pregunta
class VistaDetalle(generic.DetailView):
    model = Pregunta
    template_name = "polls/detail.html"
    context_object_name = "pregunta"

# Resultados de la votación
class VistaResultados(generic.DetailView):
    model = Pregunta
    template_name = "polls/results.html"
    context_object_name = "pregunta"

# Vista de votación
def votar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        opcion_seleccionada = pregunta.opcion_set.get(pk=request.POST["choice"])
    except (KeyError, Opcion.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "pregunta": pregunta,
                "error_message": "No seleccionaste una opción.",
            },
        )
    else:
        opcion_seleccionada.votos = F("votos") + 1
        opcion_seleccionada.save()
        return HttpResponseRedirect(reverse("polls:resultados", args=(pregunta.id,)))

# Crear pregunta
def crear_pregunta(request):
    if request.method == "POST":
        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.fecha_publicacion = timezone.now()
            pregunta.save()
            return redirect("polls:agregar_opcion", pregunta_id=pregunta.id)
    else:
        form = PreguntaForm()
    return render(request, "polls/create_question.html", {"form": form})

# Agregar opciones a una pregunta
def agregar_opcion(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)

    if request.method == "POST":
        form = OpcionForm(request.POST)
        if form.is_valid():
            opcion = form.save(commit=False)
            opcion.pregunta = pregunta
            opcion.votos = 0
            opcion.save()
            return redirect("polls:agregar_opcion", pregunta_id=pregunta.id)
    else:
        form = OpcionForm()

    opciones = pregunta.opcion_set.all()
    return render(
        request,
        "polls/add_choice.html",
        {
            "pregunta": pregunta,
            "form": form,
            "opciones": opciones,
        },
    )