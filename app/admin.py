from django.contrib import admin

# Register your models here.
from app.models import Home, About, Contact, SocialNetwork, Experience, Skills, Services, Portfolio, Blog, Visit, ForPdf

admin.site.register([Home, About, SocialNetwork, Experience,
                     Skills, Services, Portfolio, Blog, Contact, Visit,ForPdf])
