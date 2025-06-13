
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from vcms_app.models import (
    Page, Section, Block,
    TextContent, ServiceContent, StatContent,
    ProjectContent, TestimonialContent, StepContent
)

class Command(BaseCommand):
    help = "Importe la landing page Agence Web Django en base"

    def handle(self, *args, **options):
        # 1. Création de la page principale
        page = Page.objects.create(
            title="Accueil Agence Django",
            slug="accueil-agence-django",
            published=True
        )

        # 2. Création d'une section principale (tout sur une section, à adapter si besoin)
        section = Section.objects.create(
            page=page,
            title="Landing principale",
            order=0
        )

        # 3. Création des contenus spécifiques
        text_hero = TextContent.objects.create(
            title="Nous transformons vos idées en applications web performantes avec Django.",
            body="Spécialisés dans les solutions e-commerce, gestion de stock et CRM."
        )
        text_clients = TextContent.objects.create(
            title="Ils nous font confiance",
            body=""
        )
        service = ServiceContent.objects.create(
            title="Solutions digitales complètes",
            description="Nous offrons des solutions digitales complètes adaptées à vos besoins métiers.",
            icon="fa-solid fa-cogs"
        )
        text_pourquoi = TextContent.objects.create(
            title="Pourquoi choisir Django pour vos projets web ?",
            body=""
        )
        expertise = ExpertiseContent.objects.create(
            title="",
            description="Sécurité, rapidité, scalabilité et communauté active."
        )
        stat = StatContent.objects.create(
            label="Projets réalisés",
            value="120+"
        )
        text_projets = TextContent.objects.create(
            title="Découvrez une sélection de nos projets récents réalisés avec Django",
            body=""
        )
        project = ProjectContent.objects.create(
            title="Plateforme e-commerce",
            description="Développement d'une plateforme e-commerce sur-mesure avec Django.",
            link="https://exemple.com",
            date="2024-10-01"
        )
        text_avis = TextContent.objects.create(
            title="Découvrez ce que nos clients pensent de notre collaboration.",
            body=""
        )
        testimonial = TestimonialContent.objects.create(
            author="Jean Dupont",
            position="Directeur IT",
            quote="Collaboration efficace, résultats au rendez-vous !"
        )
        text_metho = TextContent.objects.create(
            title="Une méthodologie éprouvée pour atteindre vos objectifs",
            body=""
        )
        step = StepContent.objects.create(
            title="Analyse",
            description="Compréhension de vos besoins et objectifs.",
            order=0
        )
        text_contact = TextContent.objects.create(
            title="Contactez-nous pour une consultation gratuite et obtenez un devis personnalisé en 48h.",
            body="Demander un devis"
        )
        text_footer = TextContent.objects.create(
            title="Vous avez un projet en tête ? Discutons-en pour trouver la meilleure solution technique et fonctionnelle.",
            body="15 Rue de la Paix, 75002 Paris\n01 23 45 67 89\n09 87 65 43 21 (mobile)\ncontact@djangowave.com"
        )

        # 4. Récupérer les ContentTypes
        ct_text = ContentType.objects.get_for_model(TextContent)
        ct_service = ContentType.objects.get_for_model(ServiceContent)
        ct_expertise = ContentType.objects.get_for_model(ExpertiseContent)
        ct_stat = ContentType.objects.get_for_model(StatContent)
        ct_project = ContentType.objects.get_for_model(ProjectContent)
        ct_testimonial = ContentType.objects.get_for_model(TestimonialContent)
        ct_step = ContentType.objects.get_for_model(StepContent)

        # 5. Création des blocs dans l'ordre de la landing page
        Block.objects.create(section=section, order=0, content_type=ct_text, object_id=text_hero.id)
        Block.objects.create(section=section, order=1, content_type=ct_text, object_id=text_clients.id)
        Block.objects.create(section=section, order=2, content_type=ct_service, object_id=service.id)
        Block.objects.create(section=section, order=3, content_type=ct_text, object_id=text_pourquoi.id)
        Block.objects.create(section=section, order=4, content_type=ct_expertise, object_id=expertise.id)
        Block.objects.create(section=section, order=5, content_type=ct_stat, object_id=stat.id)
        Block.objects.create(section=section, order=6, content_type=ct_text, object_id=text_projets.id)
        Block.objects.create(section=section, order=7, content_type=ct_project, object_id=project.id)
        Block.objects.create(section=section, order=8, content_type=ct_text, object_id=text_avis.id)
        Block.objects.create(section=section, order=9, content_type=ct_testimonial, object_id=testimonial.id)
        Block.objects.create(section=section, order=10, content_type=ct_text, object_id=text_metho.id)
        Block.objects.create(section=section, order=11, content_type=ct_step, object_id=step.id)
        Block.objects.create(section=section, order=12, content_type=ct_text, object_id=text_contact.id)
        Block.objects.create(section=section, order=13, content_type=ct_text, object_id=text_footer.id)

        self.stdout.write(self.style.SUCCESS("Landing page Agence Web Django importée avec succès !"))
