from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home',
        'description': 'Welcome to Pernik, a city in western Bulgaria.',
        'items': [
            'Read local news and announcements from Pernik.',
            'Meet the representatives of Pernik Municipality.',
            'Discover the city’s history and cultural heritage.',
            'Find useful municipal contact information.',
        ]
    }
    return render(request, 'city/section.html', context)


def news(request):
    context = {
        'title': 'Pernik News',
        'description': 'Local updates and events in Pernik, Bulgaria.',
        'items': [
            'Visit the Municipality of Pernik website for current announcements.',
            'Pernik hosts the annual Surva International Festival of Masquerade Games.',
            'The Municipal Council publishes local decisions and public notices.',
            'Municipal services share updates about projects and city infrastructure.',
        ]
    }
    return render(request, 'city/section.html', context)


def management(request):
    context = {
        'title': 'Municipal Leadership',
        'description': 'Elected and appointed representatives serving Pernik Municipality.',
        'items': [
            'Mayor: Stanislav Vladimirov.',
            'Deputy mayors: Sashko Iliev, Stefan Krastev, and Adrian Skrimov.',
            'Municipal Secretary: Ivo Simeonov.',
            'Municipal Council Chair: Denislav Zahariev.',
            'Deputy Council Chairs: Ralitsa Andreeva and Dimitar Kolev.',
        ]
    }
    return render(request, 'city/section.html', context)


def facts(request):
    context = {
        'title': 'Facts About Pernik',
        'description': 'A few facts about Pernik and its surroundings.',
        'items': [
            'Pernik is in western Bulgaria, about 30 kilometres from Sofia.',
            'The Struma River flows through the city.',
            'The region has a long history of brown-coal mining and industry.',
            'Pernik is known for Surva, its international masquerade-games festival.',
        ]
    }
    return render(request, 'city/section.html', context)


def contacts(request):
    context = {
        'title': 'Municipal Contacts',
        'description': 'Contact details for Pernik Municipality and emergency services.',
        'items': [
            'Pernik Municipality: 1 St. Ivan Rilski Square, Pernik, Bulgaria.',
            'Municipality phone: +359 76 602 933.',
            'Email: obshtina@pernik.bg.',
            'Emergency services in Bulgaria: 112.',
        ]
    }
    return render(request, 'city/section.html', context)


def history(request):
    context = {
        'title': 'History of Pernik',
        'description': 'An introduction to the history and heritage of Pernik.',
        'items': [
            'Pernik grew into an important industrial centre as the region’s coal resources were developed.',
            'The city’s industrial heritage shaped its growth and local identity.',
            'Pernik’s cultural calendar includes the long-running Surva masquerade tradition.',
            'The city is located in the Struma River valley, close to Sofia.',
        ]
    }
    return render(request, 'city/section.html', context)


def history_people(request):
    context = {
        'title': 'People of Pernik',
        'description': 'Representatives and community members connected with Pernik.',
        'items': [
            'Mayor Stanislav Vladimirov leads the municipal administration.',
            'Municipal Council Chair Denislav Zahariev leads the elected council.',
            'Deputy mayors Sashko Iliev, Stefan Krastev, and Adrian Skrimov support municipal work.',
        ]
    }
    return render(request, 'city/section.html', context)


def history_photos(request):
    context = {
        'title': 'Historical Photos',
        'description': 'Photographs documenting Pernik in different periods.',
        'items': [
            'Historic streets of Pernik.',
            'The city centre and its public squares.',
            'Buildings and landmarks from Pernik’s past.',
        ]
    }
    return render(request, 'city/section.html', context)