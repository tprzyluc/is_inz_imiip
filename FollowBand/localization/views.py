from django.shortcuts import render

from .models import Localization
# Create your views here.




def localizationView(request):
    #form = LocalizationForm()
    localizations = Localization.objects.all()
    chujek = "kupsztal"
    context = {
        'localizations': localizations,
        'arg': chujek
    }
    #args = {'form': form, 'localizations': localizations}
    return render(request, "detail.html", context)
