from django.contrib import admin
from .models import Advertisement
from django.db.models.query import QuerySet

class AdvertisementAdmin(admin.ModelAdmin):
   list_display = ['id','title','description','price','auction','updated_date', 'created_date']  
   list_filter = ['auction', 'created_at']
   actions = ['make_auction_as_false','make_auction_as_true']
  
   fieldsets = (
      (
         'Общее',
         {
            'fields':('title','description') 
         }
      ),
      (
         'Финансы',
         {
            'fields':('price','auction'), 
            'classes':['collapse'], 
            'description':'Блок финансов'
         }
      )
   )

   @admin.action(description='Убрать возможность торга')
   def make_auction_as_false(self,request,queryset:QuerySet):
      queryset.update(auction = False)


   @admin.action(description='Добавить возможность торга')
   def make_auction_as_true(self,request,queryset:QuerySet):
      queryset.update(auction = True)   
 
admin.site.register(Advertisement, AdvertisementAdmin)

# py manage.py createsuperuser - создание аккаунта админа
# py manage.py runserver
# http://127.0.0.1:8000/admin