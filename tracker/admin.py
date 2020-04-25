from django.contrib import admin
from .models import Localite, Pays, Conseil

# Register your models here.
class Locailtet(admin.TabularInline):
    model = Localite
    extra = 0

@admin.register(Pays)
class Paysta(admin.ModelAdmin):
    list_display = ('nom','_localite')
    inlines = [Locailtet]
    def _localite(self, obj):
      return   obj.localite_pays.all().count()


class Lo(admin.ModelAdmin):
    list_display = ('nom','pays','cas_declare','cas_confirme','nombre_deces')

class Co(admin.ModelAdmin):
    list_display = ('description','status')


admin.site.register(Localite, Lo)
admin.site.register(Conseil),Co