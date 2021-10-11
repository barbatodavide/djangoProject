from django.shortcuts import render
from .models import Roll
# Create your views here.
def rolls(request):
    rolls = Roll.objects.all() # serve ad estrarre tutti gli oggetti Roll dal database
    return render(request, 'polls/sushi-rolls.html', {'rolls' : rolls})

def contattaci(request):
    return render(request, 'polls/contattaci.html')