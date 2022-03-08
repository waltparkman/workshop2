from django.contrib import admin

from tutorials.models import Customers

@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ("company_name__startswith",)
    list_display = ("company_name", "contact_name", "city", "country", "view_orders_link")
    list_filter = ("country",)

    def view_orders_link(self, obj):
        pass
        #count = obj.order_set.count()
        #url = (
        #    reverse("admin:tutorials_order_changelist")
        #    + "?"
        #    +urlencode({"customer__id": f"{obj.id}"})
        #)
        #return format_html('<a href="{}">{} Orders</a>', url, count)

    view_orders_link.short_description = "Orders"
