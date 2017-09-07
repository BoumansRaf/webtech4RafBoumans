
from pymongo import MongoClient
from djangotoolbox.fields import ListField





    def addRecept(request):
        client = MongoClient()
        db = client.receptdb




        if request.method == 'POST':
            name = request.POST.get('name')
            cals = request.POST.get('cals')
            ingredients = request.POST.get('ingredients')
            time = request.POST.get('time')


            recept = db.find_one({"name":  + name  })
            if recept == None:
                recept = name + ' Cals:' + cals + ' ingredients:' + ingredients + ' time:' + time
                post = {"name:"  name , "cals:" cals, "ingredients:" ingredients, "time:" time}
            else:
                recept =  'Recept bestaat al'


            return render(request, 'recepten/index.html', {'recept': recept} )
        else:
                return render(request, 'recepten/index.html', None)
