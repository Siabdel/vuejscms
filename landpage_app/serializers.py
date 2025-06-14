
from rest_framework import serializers
from .models import Page, Section, MBlock, TextContent, ServiceContent, StatContent, ProjectContent, TestimonialContent, StepContent
from django.contrib.contenttypes.models import ContentType

# Sérialise chaque type de contenu
class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = ['id', 'title', 'body']

class ServiceContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContent
        fields = ['id', 'title', 'description', 'icon']

class StatContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatContent
        fields = ['id', 'label', 'value']

class ProjectContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectContent
        fields = ['id', 'title', 'description', 'link', 'date']

class TestimonialContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialContent
        fields = ['id', 'author', 'position', 'quote']

class StepContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepContent
        fields = ['id', 'title', 'description', 'order']

# Sérialiseur polymorphe pour MBlock
class MBlockSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = MBlock
        fields = ['id', 'order', 'content']

    def get_content(self, obj):
        model = obj.content_type.model
        if model == 'textcontent':
            return TextContentSerializer(obj.content_object).data
        elif model == 'servicecontent':
            return ServiceContentSerializer(obj.content_object).data
        elif model == 'statcontent':
            return StatContentSerializer(obj.content_object).data
        elif model == 'projectcontent':
            return ProjectContentSerializer(obj.content_object).data
        elif model == 'testimonialcontent':
            return TestimonialContentSerializer(obj.content_object).data
        elif model == 'stepcontent':
            return StepContentSerializer(obj.content_object).data
        return None

class SectionSerializer(serializers.ModelSerializer):
    mblocks = MBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'order', 'mblocks']

class PageSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'sections']
