from django.contrib import admin
from .models import Propriete,Voiture,AutoMobile
# Register your models here.
class AdminPropriete(admin.ModelAdmin):
    list_display = ('NNI','Prenom','Nom','tel')

class AdminVoiture(admin.ModelAdmin):
    list_display = ('plaque','marque','genre','couleur')

admin.site.register(Propriete,AdminPropriete)
admin.site.register(Voiture,AdminVoiture)

admin.site.register(AutoMobile)
