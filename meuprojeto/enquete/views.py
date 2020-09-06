from django.shortcuts import render
from django.http import HttpResponse
from enquete.models import Enquete

# Create your views here.
def index(request):
    return HttpResponse('Hello!!')


def bemvindo(request):
    return render(request, 'bemvindo.html')


def enquete(request, enquete_id):
    #enquete = Enquete()
    enquete = Enquete.objects.get(id=enquete_id)
    # if enquete_id == 1:
    #    enquete = Enquete('Qual grau de escolaridade?', '24/08/2020')
    #if enquete_id == 2:
    #    enquete = Enquete('Qual sua opinião sobre o atual governo?', '25/08/2020')
    #if enquete_id == 3:
    #    enquete = Enquete('Qual sua posição sobre aulas presencias no ano de 2020?', '26/08/2020')
    
    return render(request, 'enquete.html', { "enquete" : enquete})