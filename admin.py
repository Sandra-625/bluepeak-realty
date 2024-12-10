from django.contrib import admin
from.models import Property
from.models import Agent





# Register your models here.
def register_models():
    from .models import Property
    Property = apps.get_model('properties', 'property')
    admin.site.register(Property)

    register_models()



class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'image', 'status', 'bedrooms', 'bathrooms', 'square_feet')
    search_fields = ('title', 'location', 'status')

admin.site.register(Property, PropertyAdmin)

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'phone', 'preview_image')
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="height: 100px; object-fit: cover;" />'
        return "No Image"
    preview_image.allow_tags = True
    preview_image.short_description = "Image Preview"



