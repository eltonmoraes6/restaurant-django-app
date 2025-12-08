from Base_App.models import PageSection

defaults = [
    ("home", "hero_title", "Welcome to Burgger Restaurant!"),
    ("home", "hero_subtitle", "The best burgers in your city."),
    ("about", "description", "We began our journey in 1990..."),
    ("footer", "contact_text", "Contact us anytime."),
]

for page, section, content in defaults:
    PageSection.objects.get_or_create(
        page=page,
        section=section,
        defaults={'content': content}
    )

print("Default CMS content created!")
