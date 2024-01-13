from django.shortcuts import render,HttpResponse
from .forms import PakCardForm,BalajiCardForm
from django.http import FileResponse
from .models import Pak_IdCard,Template,Balaji_IdCard
from .idmaker import IdMaker
from django.templatetags.static import static
import requests


def pak_idcard(request):
    if request.method == 'POST':
        form = PakCardForm(request.POST, request.FILES)
        if form.is_valid():
            idcard = form.save()
            template=IdMaker.pak_id_card(idcard)
            idcard.image.delete()
            #tempModel= Template(template,pk=idcard.pk)
            #tempModel.save()
            template.save('myapp/static/template/pak/{}.png'.format(idcard.pk))
            return render(request, 'myapp/pak_idcard_download.html', {'idcard': idcard})

    else:
        form = PakCardForm()
    return render(request, 'myapp/pak_id_card.html', {'form': form})


def balaji_idcard(request):
    if request.method == 'POST':
        form = BalajiCardForm(request.POST, request.FILES)
        if form.is_valid():
            idcard = form.save()
            template=IdMaker.balaji_id_card(idcard)
            idcard.image.delete()
            #tempModel= Template(template,pk=idcard.pk)
            #tempModel.save()
            template.save('myapp/static/template/balaji/{}.png'.format(idcard.pk))
            return render(request, 'myapp/balaji_idcard_download.html', {'idcard': idcard})

    else:
        form = BalajiCardForm()
    return render(request, 'myapp/balaji_id_card.html', {'form': form})


def pak_idcard_download(request, pk):
    idcard = Pak_IdCard.objects.get(pk=pk)

    # tempcard=Template.objects.get(pk=pk)
    file = open('myapp/static/template/pak/{}.png'.format(idcard.pk), 'rb')
    # file = open('media/templates/{}'.format(tempcard.template), 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename={}.png'.format(idcard.name)
    return response

def balaji_idcard_download(request, pk):
    idcard = Balaji_IdCard.objects.get(pk=pk)

    # tempcard=Template.objects.get(pk=pk)
    file = open('myapp/static/template/balaji/{}.png'.format(idcard.pk), 'rb')
    # file = open('media/templates/{}'.format(tempcard.template), 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename={}.png'.format(idcard.name)
    return response



def temp(request):
    img_url=static('template/pak_template.png')
    return render(request,"myapp/index1.html", {'img_url':img_url})


def idcard_home(request):
   # image_url1 = "https://i.ibb.co/qx81ryS/balaji-clg.png"
    #image_url2 = "https://i.ibb.co/sm643C0/pak-temp.png"
    #response1 = requests.get(image_url1)
    #response2 = requests.get(image_url2)
    #with open("balaji-clg.png", "wb") as f:
     #   f.write(response1.content)

    #with open("pak-temp.png", "wb") as f:
     #   f.write(response2.content)
    #balaji_temp_url = static('balaji-clg.png')
    #pak_temp_url = static('pak-temp.png')
    return render(request,"myapp/idcard.html")




