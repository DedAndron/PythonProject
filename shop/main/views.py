from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse, HttpResponse
from django.shortcuts import render

from . import models
from .cards import cards


# Create your views here.


def home(request):
    return render(request, 'main/index.html', {'cards': cards})


def about(request):
    text = 'Welcome to the About page!'
    frameworks = []
    return render(request, 'main/about.html',
                  {'text': text, 'frameworks': frameworks})


def get_card(request, card_id):
    if card_id < 1 or card_id > len(cards):
        return HttpResponseNotFound('Not Found')

    card = cards[card_id - 1]
    title = request.GET.get('title') or card['title']
    return render(request, 'main/card.html', {'card': card, 'title': title})


def search(request):
    title = request.GET.get('title', '').strip()
    if not title:
        return HttpResponseBadRequest('Enter a title to search.')

    query = title.casefold()
    card = next(
        (card for card in cards if query in card['title'].casefold()),
        None,
    )
    if card is None:
        return HttpResponseNotFound('Not Found')

    return render(request, 'main/card.html', {
        'card': card,
        'title': card['title'],
    })
def create_card(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        print(title, description, image)
        card = models.Card(title=title, description=description, image=image)
        card.save()
    return JsonResponse({'message':'ok'})

def registration(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = models.User(avatar=avatar, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        return JsonResponse({
            'success': True,
            'redirect_url': ''
        })
    return render(request, 'main/register.html')
