from django.db import models

# Create your models here.
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Page principale
class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Section d'une page (ex: header, services, témoignages, etc.)
class Section(models.Model):
    page = models.ForeignKey(Page, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title or 'Section'} ({self.page.title})"

# Bloc générique polymorphe (via GenericForeignKey)
class MBlock(models.Model):
    section = models.ForeignKey(Section, related_name='mblocks', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    # Polymorphisme via ContentType
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Bloc: {self.content_object}"

# --------- Modèles de contenu spécifiques (polymorphes) ---------

# Bloc de texte
class TextContent(models.Model):
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title or f"Texte #{self.id}"

# Bloc image
class ImageContent(models.Model):
    image = models.ImageField(upload_to='blocks/images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f"Image #{self.id}"

# Bloc galerie
class GalleryContent(models.Model):
    title = models.CharField(max_length=200, blank=True)
    images = models.ManyToManyField('ImageContent', related_name='galleries')

    def __str__(self):
        return self.title or f"Galerie #{self.id}"

# Bloc témoignage
class TestimonialContent(models.Model):
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    quote = models.TextField()
    photo = models.ImageField(upload_to='blocks/testimonials/', blank=True, null=True)

    def __str__(self):
        return f"{self.author} - {self.position}"

# Bloc service (exemple agence web)
class ServiceContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)  # nom de classe icône ou URL

    def __str__(self):
        return self.title

# Bloc menu (exemple restaurant)
class MenuContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class DishContent(models.Model):
    menu = models.ForeignKey(MenuContent, related_name='dishes', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='blocks/dishes/', blank=True, null=True)

    def __str__(self):
        return self.name

# Bloc statistique clé
class StatContent(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.value} {self.label}"

# Bloc étape/méthodologie
class StepContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    icon = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

# Bloc projet
class ProjectContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blocks/projects/', blank=True, null=True)
    link = models.URLField(blank=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

# Bloc média générique
class MediaContent(models.Model):
    file = models.FileField(upload_to='blocks/media/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.file.name

