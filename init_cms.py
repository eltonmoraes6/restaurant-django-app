from Base_App.models import PageSection

defaults = [
    ("home", "hero_title", "Welcome!", "The best burgers in town.", None),
    ("home", "hero_subtitle", "", "Fresh ingredients, great taste!", None),
    ("about", "description", "About Us", "We started our journey in 1990...", None),
    ("footer", "contact_text", "Contact Us", "Reach us anytime.", None),
]

for page, section, title, content, image in defaults:
    PageSection.objects.get_or_create(
        page=page,
        section=section,
        defaults={"title": title, "content": content}
    )

print("CMS defaults loaded!")
