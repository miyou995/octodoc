from django.contrib import admin
from .models import Business
from django.utils.html import format_html






# 2 Photos en haut de page a coté du grand banner
# TwoPhotos._meta.verbose_name = "2 banner haut de page a coté du grand banner (370 x 230 px )"
# TwoPhotos._meta.verbose_name_plural = "2 banner haut de page a coté du grand banner (370 x 230 px )"

# # deux banners qui sérapres les produits
# DualBanner._meta.verbose_name = "2 banner separateur de section (570 x 200 px )"
# DualBanner._meta.verbose_name_plural = "2 banner separateur de section (570 x 200 px )"

# #3 banner en haut de page en dessous de grand banner
# ThreePhotos._meta.verbose_name = "3 banner haut de page (370 x 225 px )"
# ThreePhotos._meta.verbose_name_plural = "3 banner haut de page (370 x 225 px )"

# # banner en bas de page
# LargeBanner._meta.verbose_name = " banner large Bas de page (1170 x 400 px )"
# LargeBanner._meta.verbose_name_plural = " banner large Bas de page (1170 x 400 px )"
Business._meta.verbose_name = "Informations magasin"




    # def has_add_permission(self, request):
    #     business = Business.objects.all()
    #     if business.count() > 1:
    #         return False
    #     else: 
    #         return True

    # def has_add_permission(self, request):
    #     return False

@admin.register(Business)
class BusinesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    def has_add_permission(self, request):
        business = Business.objects.all()
        if business.count() > 1:
            return False
        else: 
            return True