from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse


def index(request):
    return redirect('/question/1/')


def questions(request, pk):

    dict_of_options = {
        1: ["Tax-collector attempting to collect taxes from everyone for 'boat maintenance'", "Scientist who is studying water samples instead of helping to row the boat.", "tax-collector", "scientist"],
        2: ["Billionaire who purposefully sunk the ship to get rid of the tax-collecter, but is now offering you 1 million dollars allow him to stay on the ship.", "Pineapple-on-Pizza lover who only eats pineapple pizza and hates on all other pizzas.", "billionaire", "pineapple-on-pizza-lover"],
        3: ["Alien attempting to kidnap everyone.", "Epée fencer waiting for the 'right opportunity.", "alien", "epee-fencer"],
        4: ["Banana-duck thief that stole all the banana-ducks in the world.", "A selfish person who has fifteen sandwiches but refuses to share with everyone else.", "banana-duck-thief", "sandwich-hoarder"],
        5: ["Someone on the boat who died from the fear of being tossed overboard. Though you tossed the corpse overboard, its ghost remain on the boat, haunting the rest of the people on board. Its spirit weighs down the boat with its heavy emotions.", "Seagull that keeps pecking everybody on board because it is offended by their horrendous fashion sense.", "ghost", "seagull"],
    }


    current_options = dict_of_options[pk]


    page_range = range(pk-2, pk+3)  # This will generate the range of pages you want
    
    # Make sure that the range doesn't go below 1
    page_range = [num for num in page_range if num > 0 and num <= 5]  # Assuming 5 pages max
    




    context = {
        'pk': pk,
        'page_range': page_range,
        'current_options' : current_options,
        
    }
    return render(request, "dilemma/index.html", context)







