from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SocialNetwork(models.Model):
    image = models.ImageField(upload_to="social_network/")
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=155)

    def __str__(self):
        return self.url


class Home(models.Model):
    image = models.ImageField(upload_to="home/")
    image_icon = models.ImageField(upload_to="image_icon")
    name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    text = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to="about/")
    name = models.CharField(max_length=155)
    job = models.CharField(max_length=155)
    text = models.TextField()
    project_count = models.PositiveIntegerField()
    client = models.PositiveIntegerField()
    social_network = models.ManyToManyField(to="app.SocialNetwork",
                                            related_name="social_networks")

    def __str__(self):
        return self.name


class Experience(BaseModel):
    title = models.CharField(max_length=155)
    text = models.TextField()
    year = models.PositiveIntegerField()
    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=155)
    percentage = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Services(models.Model):
    image = models.ImageField(upload_to="services/")
    title = models.CharField(max_length=155)
    text = models.TextField()

    def __str__(self):
        return self.title


class Blog(BaseModel):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=155)
    text = models.TextField()

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    image = models.ImageField(upload_to="services/")
    title = models.CharField(max_length=155)
    link = models.CharField(max_length=200)
    customer = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Visit(models.Model):
    image = models.ImageField(upload_to="visit/")
    title = models.CharField(max_length=155)
    address = models.CharField(max_length=155)
    location = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    subject = models.CharField(max_length=155)
    text = models.TextField()

    def __str__(self):
        return self.name
