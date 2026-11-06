from django.http import HttpResponse
from django.shortcuts import render
from cards import cards

# Create your views here.

def home(request):
    return render(request, 'main/index.html', {'cards':cards})


def about(request):
    text = 'Welcome to the About page!'

    frameworks = []
    return render(request, 'main/about.html',
                  {'text': text, 'frameworks': frameworks})
def get_card(request, id):
    if id>0 and id<len(cards):
        return render(request, 'main/card.html', {'card': cards[id-1], 'title':f'Card {id}'})
    else:
        return HttpResponse("Not found")