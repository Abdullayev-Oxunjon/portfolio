from django.shortcuts import render, redirect

from app.form import ContactForm
from app.models import Home, SocialNetwork, About, Skills, Experience, Services, Portfolio, Blog


def master(table):
    return table.objects.all()


def index_view(request):
    homes = master(Home)
    social_networks = master(SocialNetwork)
    abouts = master(About)
    skills = master(Skills)
    experiences = master(Experience)
    services = master(Services)
    portfolio = master(Portfolio)
    blogs = master(Blog)


    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ContactForm()

    return render(request=request,
                  template_name="app/index.html",
                  context={"homes": homes,
                           "social_networks": social_networks,
                           "abouts": abouts,
                           "skills": skills,
                           "experiences": experiences,
                           "services": services,
                           "portfolio": portfolio,
                           "blogs": blogs,
                           "form": form})
