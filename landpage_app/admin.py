from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Page, Section, MBlock,
    TextContent, ImageContent, GalleryContent, TestimonialContent,
    ServiceContent, MenuContent, DishContent,
    StatContent, StepContent, ProjectContent, MediaContent
)

class BlockInline(admin.TabularInline):
    model = MBlock
    extra = 1

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SectionInline]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'order')
    inlines = [BlockInline]
    list_filter = ('page',)

@admin.register(MBlock)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('section', 'content_type', 'object_id', 'order')
    list_filter = ('section', 'content_type')
    ordering = ('section', 'order')

# Enregistrement des modèles de contenu polymorphes
admin.site.register(TextContent)
admin.site.register(ImageContent)
admin.site.register(GalleryContent)
admin.site.register(TestimonialContent)
admin.site.register(ServiceContent)
admin.site.register(MenuContent)
admin.site.register(DishContent)
admin.site.register(StatContent)
admin.site.register(StepContent)
admin.site.register(ProjectContent)
admin.site.register(MediaContent)

