from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Nibras',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)