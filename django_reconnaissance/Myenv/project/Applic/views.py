from django.shortcuts import render,redirect
from .models import  Propriete, Voiture
from django.contrib import messages
from .detect import detection_plaque
import os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, "index.html")

def detect(request):
    return render(request, "Block/detect.html")
#-------------- CRUD propriete -------------------
def FormP(request):
    return render(request, "Block/FormP.html")

def EditPro(request, NNI):
    propriete = Propriete.objects.get(NNI=NNI)
    return render(request,"Block/Edit.html",{"propriete":propriete})

def Edit(request,NNI):
    propriete = Propriete.objects.get(NNI=NNI)
    context = {
        "propriete":propriete,
    }
   # NNI = request.POST['NNI']
   # Prenom = request.POST['Prenom']
   # Nom = request.POST['Nom']
   # tel = request.POST['tel']
    if request.method == "GET":
        return render(request,"Block/Edit.html", context)

    if request.method == "POST":
        NNI = request.POST['NNI']
        if len(NNI) > 8:
            messages.error(request, "le numero d'identification n'est pas correcte")
            return render(request, "Block/Edit.html")
        if not NNI:
            messages.error(request, "Veuillez saisir le NNI")
            return render(request, "Block/Edit.html")
        Prenom = request.POST['Prenom']
        if not Prenom:
            messages.error(request, "Veuillez Saisir le prenom")
            return render(request, "Block/Edit.html")
        Nom = request.POST['Nom']
        if not Nom:
            messages.error(request, "Veuillez saisir le nom")
            return render(request, "Block/Edit.html")
        tel = request.POST['tel']
        if not tel:
            messages.error(request, "Veuillez saisir le numero telephone")
            return render(request, "Block/Edit.html")


        #propriete = Propriete.objects.get(NNI=NNI)
        propriete.Prenom = Prenom
        propriete.Nom = Nom
        propriete.tel = tel
        propriete.save()

        messages.success(request, "Enrigistrer avec success")

        return redirect('formp')




def AjoutProp(request):
    if request.method == "POST":
        NNI = request.POST['NNI']
        if len(NNI) > 8:
            messages.error(request, "le numero d'identification n'est pas correcte")
            return render(request, "Block/FormP.html")
        if len(NNI) < 8:
            messages.error(request, "le numero d'identification n'est pas correcte")
            return render(request, "Block/FormP.html")
        if not NNI:
            messages.error(request, "Veuillez saisir le NNI")
            return render(request, "Block/FormP.html")
        Prenom = request.POST['Prenom']
        if not Prenom:
            messages.error(request, "Veuillez Saisir le prenom")
            return render(request, "Block/FormP.html")
        Nom = request.POST['Nom']
        if not Nom:
            messages.error(request, "Veuillez saisir le nom")
            return render(request, "Block/FormP.html")
        tel = request.POST['tel']
        if not tel:
            messages.error(request, "Veuillez saisir le numero telephone")
            return render(request, "Block/FormP.html")

        Propriete.objects.create(NNI=NNI,Prenom=Prenom,Nom=Nom,tel=tel)
        messages.success(request, "Enrigistrer avec success")

        return redirect('formp')



def ModProp(request):
    pass

def AffiProp(request):
    Proprietes = Propriete.objects.all()

    context = {
        'Proprietes': Proprietes
    }
    return render(request,"Block/AffiP.html",context)

def SuppProp(request, id):
    propriete = Propriete.objects.get(pk=id)
    propriete.delete()

    messages.error(request,"Element supprimer")
    return  redirect('affpro')

# ----------------------CRUD Voiture ----------------------



def FormVo(request):
    x={
        "Proprietes"  : Propriete.objects.all()
    }
    return render(request, "Block/FormVo.html",x)


def AjoutVoit(request):
    return render(request, "Block/FormVo.html")




def AjoutV(request):
  if request.method == 'POST':
    #   plaque = request.POST['plaque']
    #   if not plaque:
    #       messages.warning(request, "Veuillez ajoutez le numero du plaque")
    #       return  render(request,"Block/FormVo.html")
     # elif plaque == plaque:
     #     messages.error(request, "Cette numero existe deja dans la BD")
     #     return render(request, "Block/FormVo.html")
      propriete = request.POST['propriete']
      if not propriete:
          messages.warning(request, "la case du propriete est vide")
          return render(request, "Block/FormVo.html")
      marque = request.POST['marque']
      if not marque:
          messages.error(request, "Veuillez ajoutez le nom du marque")
          return render(request, "Block/FormVo.html")

      genre = request.POST['genre']
      if not genre:
          messages.error(request, "Veuillez Saisir le modele")
          return render(request, "Block/FormVo.html")

      couleur = request.POST['couleur']
      if not couleur:
          messages.error(request, "Veuillez Saisir la couleur")
          return render(request, "Block/FormVo.html")

      image = request.FILES['img']
      if not image:
          messages.error(request, "Veuillez ajouter une image du voiture")
          return render(request, "Block/FormVo.html")

      voiture = Voiture.objects.create(propriete= Propriete.objects.get(NNI=propriete), marque=marque, genre=genre,
                                     couleur=couleur,
                           image=image)
      voiture.save()
      messages.success(request, "Voiture Enrigistrer avec success")

      image_path = str(settings.BASE_DIR) + '/media/' + voiture.image.name
      detect_text = detection_plaque(image_path)

      voiture.plaque = detect_text
      voiture.save()

      return redirect('formV')

def ModVoit(request, id):
    print(id)
    voit = Voiture.objects.get(pk=id)
    context = {
        'voit' : voit,
        "Proprietes"  : Propriete.objects.all().exclude(pk=voit.propriete.NNI)
    }

    if request.method == 'POST':
        # plaque_input = request.POST['plaque']
        # if not plaque_input:
        #     messages.warning(request, "Veuillez ajoutez le numero du plaque")
        #     return render(request, 'Block/ModVoit.html', context)
        # elif plaque == plaque:
        #     messages.error(request, "Cette numero existe deja dans la BD")
        #     return render(request, "Block/FormVo.html")
        propriete = request.POST['propriete']
        if not propriete:
            messages.warning(request, "la case du propriete est vide")
            return render(request, 'Block/ModVoit.html', context)
        marque = request.POST['marque']
        if not marque:
            messages.error(request, "Veuillez ajoutez le nom du marque")
            return render(request, 'Block/ModVoit.html', context)

        genre = request.POST['genre']
        if not genre:
            messages.error(request, "Veuillez Saisir le modele")
            return render(request, 'Block/ModVoit.html', context)

        couleur = request.POST['couleur']
        if not couleur:
            messages.error(request, "Veuillez Saisir la couleur")
            return render(request, 'Block/ModVoit.html', context)


        voiture = Voiture.objects.get(pk=id)
        # voiture.plaque=plaque_input
        voiture.propriete= Propriete.objects.get(NNI=propriete)
        voiture.marque=marque
        voiture.genre=genre
        voiture.couleur=couleur
        voiture.save()
        messages.success(request, "Voiture modifier avec success")

        return redirect('AffichVoit')

    return render(request, 'Block/ModVoit.html', context)



def AffichVoit(request):
    Voit = Voiture.objects.all()
    return render(request, "Block/AffiVo.html",{'Voit':Voit})

def SuppVoit(request, id):
    Voiture.objects.get(pk=id).delete()
    return redirect("AffichVoit")