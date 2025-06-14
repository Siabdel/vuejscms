from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from landpage_app.models import (
    Page, Section, MBlock,
    TextContent, ServiceContent, StatContent, ProjectContent,
    TestimonialContent, StepContent
)

class Command(BaseCommand):
    help = "Importe des données de test pour la landing page agence web Django (avec services, projets, menus)"

    def handle(self, *args, **options):
        # 1. Page
        page = Page.objects.create(
            title="Accueil Agence Django",
            slug="accueil-agence-django",
            published=True
        )

        # 2. Section principale
        section = Section.objects.create(
            page=page,
            title="Landing principale",
            order=0
        )

        # 3. Contenus spécifiques
        text_hero = TextContent.objects.create(
            title="Nous transformons vos idées en applications web performantes avec Django.",
            body="Spécialisés dans les solutions e-commerce, gestion de stock et CRM."
        )
        stat = StatContent.objects.create(
            label="Projets réalisés",
            value="120+"
        )
        testimonial = TestimonialContent.objects.create(
            author="Jean Dupont",
            position="Directeur IT",
            quote="Collaboration efficace, résultats au rendez-vous !"
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

        # 4. Plusieurs services
        services = []
        service_data = [
            ("E-commerce", "Solutions e-commerce performantes avec paiement sécurisé, gestion des stocks et expérience client optimale.", "shopping-cart"),
            ("Gestion de stock", "Systèmes de gestion d'inventaire en temps réel avec alertes et prévisions pour optimiser vos stocks.", "boxes"),
            ("CRM sur mesure", "Outils de gestion de la relation client adaptés à votre secteur d'activité avec automatisation des processus.", "users"),
            ("ERP", "Systèmes de gestion intégrés pour optimiser l'ensemble de vos processus métiers.", "chart-line"),
            ("Solutions immobilières", "Plateformes spécialisées pour agences immobilières avec gestion des biens, rendez-vous et visites virtuelles.", "home"),
            ("CMS personnalisé", "Systèmes de gestion de contenu adaptés à vos besoins avec éditeur intuitif pour vos équipes.", "file-alt"),
        ]
        for title, desc, icon in service_data:
            services.append(ServiceContent.objects.create(title=title, description=desc, icon=icon))

        # 5. Plusieurs projets
        projects = []
        project_data = [
            ("E-commerce Mode Luxe", "Plateforme e-commerce haut de gamme avec système de recommandation IA", "https://images.unsplash.com/photo-1607082352122-fa4437c95f25?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", "2024-01-10"),
            ("Gestion de stock B2B", "Solution complète de gestion d'inventaire pour distributeur", "https://images.unsplash.com/photo-1486401899868-0e435ed85128?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", "2023-07-22"),
            ("Solution CRM Immobilier", "Outil de gestion clientèle pour réseau d'agences immobilières", "https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", "2023-03-30"),
        ]
        for title, desc, img, date in project_data:
            projects.append(ProjectContent.objects.create(title=title, description=desc, link=img, date=date))

        # 6. Exemple de menu (optionnel, pour montrer la flexibilité)
        # Ajoute ce modèle dans models.py si tu veux l'utiliser :
        # class MenuContent(models.Model):
        #     title = models.CharField(max_length=200)
        #     description = models.TextField(blank=True)
        #     def __str__(self): return self.title
        # menu = MenuContent.objects.create(
        #     title="Menu du jour",
        #     description="Entrée, plat, dessert pour 18€"
        # )

        # 7. ContentTypes
        ct_text = ContentType.objects.get_for_model(TextContent)
        ct_service = ContentType.objects.get_for_model(ServiceContent)
        ct_stat = ContentType.objects.get_for_model(StatContent)
        ct_project = ContentType.objects.get_for_model(ProjectContent)
        ct_testimonial = ContentType.objects.get_for_model(TestimonialContent)
        ct_step = ContentType.objects.get_for_model(StepContent)
        # ct_menu = ContentType.objects.get_for_model(MenuContent)  # si activé

        # 8. MBlocks (ordre logique)
        order = 0
        MBlock.objects.create(section=section, order=order, content_type=ct_text, object_id=text_hero.id); order += 1
        MBlock.objects.create(section=section, order=order, content_type=ct_stat, object_id=stat.id); order += 1
        for service in services:
            MBlock.objects.create(section=section, order=order, content_type=ct_service, object_id=service.id)
            order += 1
        for project in projects:
            MBlock.objects.create(section=section, order=order, content_type=ct_project, object_id=project.id)
            order += 1
        MBlock.objects.create(section=section, order=order, content_type=ct_testimonial, object_id=testimonial.id); order += 1
        MBlock.objects.create(section=section, order=order, content_type=ct_step, object_id=step.id); order += 1
        # MBlock.objects.create(section=section, order=order, content_type=ct_menu, object_id=menu.id); order += 1  # si menu activé
        MBlock.objects.create(section=section, order=order, content_type=ct_text, object_id=text_contact.id); order += 1
        MBlock.objects.create(section=section, order=order, content_type=ct_text, object_id=text_footer.id)

        self.stdout.write(self.style.SUCCESS("Données de test landing page (avec services, projets) importées avec succès !"))
