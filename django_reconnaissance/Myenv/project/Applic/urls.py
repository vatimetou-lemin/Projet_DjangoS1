from django.urls  import path
from .views import  *
urlpatterns = [
    path('',home,name='home'),
    path('AjoutV/',AjoutV,name='AjoutV'),
    path('AffichVoit/',AffichVoit,name='AffichVoit'),
    path('affPro/',AffiProp,name='affPro'),
    path('formp',FormP,name='formp'),
    path('ajoutprop',AjoutProp,name='ajoutprop'),
    path('detect',detect,name='detect'),
    path('editP/<NNI>',EditPro,name='editP'),
    path('Edit/<int:NNI>',Edit,name='EditP'),
    path('suppProp/<int:NNI>',SuppProp,name='suppProp'),
    path('formV',FormVo,name='formV'),
    path('suppVoiture/<int:id>',SuppVoit,name='suppVoiture'),
    path('ModVoit/<int:id>',ModVoit,name='ModVoit')
]