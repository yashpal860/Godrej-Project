from django.contrib import admin
from .models import Contact, Enquiry, Contact_us, BrochureRequest



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'submitted_at']
    search_fields = ['name', 'email']
    
admin.site.register(Enquiry)

admin.site.register(Contact_us)

@admin.register(BrochureRequest)
class BrochureRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city', 'created_at')
    search_fields = ('name', 'email', 'phone', 'city')
    list_filter = ('created_at',)
    readonly_fields = ('name', 'email', 'phone', 'city', 'message', 'created_at')

    def has_add_permission(self, request):
        return False  # Optional: Disable adding via admin

    def has_change_permission(self, request, obj=None):
        return False  # Optional: Make records read-only