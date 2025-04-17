from django.shortcuts import render

# Aqui fica a primeira view
def index(request):

    return render(
        request,
        'global/base.html',
    )

def nome(request):
    return render(
        request,
        'seunome.html'
    )
# REQUEST - RESPONSE - RENDER