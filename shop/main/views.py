from django.shortcuts import render

# Create your views here.

def home(request):
    cards = [
        {
            'image': 'main/images/UwU1.png',
            'title': 'UwU1',
            'text': 'Картка з зображенням UwU1.',
        },
        {
            'image': 'main/images/gisan.png',
            'title': 'gisan',
            'text': 'Картка з зображенням gisan.',
        },
        {
            'image': 'main/images/gsdn.png',
            'title': 'gsdn',
            'text': 'Картка з зображенням gsdn.',
        },
    ]
    return render(request, 'main/index.html', {'cards': cards})


def about(request):
    text = 'Welcome to the About page!'
    frameworks = []
    return render(request, 'main/about.html',
                  {'text': text, 'frameworks': frameworks})