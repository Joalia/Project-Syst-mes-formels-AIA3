"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Acceuil.urls')),
    path('Acceuil',include('Acceuil.urls')),
    path('Dashboard',include('Dashboard.urls')),
    path('app',include('app.urls')),
    path('Profil',include('Profil.urls')),
    path('Antecedents_medicaux',include('Antécédents_médicaux.urls')),
    path('Cardio',include('Cardio.urls')),
    path('Consultations',include('Consultations.urls')),
    path('Fiche_medicale',include('Fiche_medicale.urls')),
    path('Whatsapp',include('Whatsapp.urls')),
    path('Connexion',include('Deconnexion.urls')),
    path('Connexion',include('Connexion.urls')),
    path('Cycle_menstruel', include('Cycle_menstruel.urls')),
    path('Help', include('Help.urls')),
    path('Actu_sante', include('Actu_sante.urls')),
    path('Soins_de', include('Soins_de.urls')),

]
