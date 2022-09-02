import pkg_resources

from tutor import hooks

from .__about__ import __version__


################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__,
        "WELCOME_MESSAGE": "Continue aprendendo. Persiga sua paixão. Avance sua carreira.",
        "PRIMARY_COLOR": "#012646",  # cool blue
        # Footer links are dictionaries with a "title" and "url"
        # To remove all links, run:
        # tutor config save --set INDIGO_FOOTER_NAV_LINKS=[] --set INDIGO_FOOTER_LEGAL_LINKS=[]
        "FOOTER_NAV_LINKS": [
            {"title": "Sobre", "url": "https://www.projectcompany.org/projectuniversity"},
			{"title": "Programa de Afiliados", "url": "https://www.projectcompany.org/programaafiliadospu"},
			{"title": "Parceiros", "url": "https://www.projectcompany.org/parceiros"},
			{"title": "Gratuito Para Quem Precisa", "url": "https://www.projectcompany.org/freeprojectuniversity"},
            {"title": "Contato", "url": "https://www.projectcompany.org/contato"},
        ],
        "FOOTER_LEGAL_LINKS": [
            {"title": "Termos de Serviço e Código de Honra", "url": "https://www.projectcompany.org/companypolicies"},
        ],
    },
    "unique": {},
    "overrides": {},
}

# Theme templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutorindigo", "templates")
)
# This is where the theme is rendered in the openedx build directory
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("indigo", "build/openedx/themes"),
    ],
)

# Force the rendering of scss files, even though they are included in a "partials" directory
hooks.Filters.ENV_PATTERNS_INCLUDE.add_item(r"indigo/lms/static/sass/partials/lms/theme/")

# Load all configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"INDIGO_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"INDIGO_{key}", value) for key, value in config["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))
