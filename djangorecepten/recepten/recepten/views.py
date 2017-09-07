from django.db import models

from djangotoolbox.fields import ListField


class Post(models.Model):
    name = models.CharField()
    cals = models.IntegerField()
    ingredients = ListField()
    time = TextField()

    def addRecept(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            cals = request.POST.get('cals')
            ingredients = request.POST.get('ingredients')
            time = request.POST.get('time')


            recept = db.get('name:' + name)
            if recept == None:
                recept = name + ' Cals:' + cals + ' ingredients:' + ingredients + ' time:' + time
            else:
                recept =  'Recept bestaat al'


                return render(request, 'recepten/index.html', {'recept': recept} )
        else:
                return render(request, 'recepten/index.html', None)
