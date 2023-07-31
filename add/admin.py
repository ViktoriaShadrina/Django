from django.contrib import admin
# from .models import Test
from .models import Advertisement
# импортирую класс для подсказок 
from django.db.models.query import QuerySet


#  admin_class - класс для кастомизации
class AdvertisementAdmin(admin.ModelAdmin):
   # отображение в витде таблицы
   list_display = ['id','title','description','price','auction','updated_date', 'created_date']  
   # параметры фильтрации
   list_filter = ['auction', 'created_at']
   #добавляю функции  лдля выбранных записей
   actions = ['make_auction_as_false','make_auction_as_true']
   # создание блоков
   fieldsets = (
      (#1 блок
         'Общее',# название блока
         {
            'fields':('title','description') # поля блока
         }
      ),
      (#2 блок
         'Финансы',# название блока
         {
            'fields':('price','auction'), # поля блока
            'classes':['collapse'], # функционал скрытия блока
            'description':'Блок финансов' #подсказка о блоке
         }
      )
   )





   @admin.action(description='Убрать возможность торга')
   def make_auction_as_false(self,request,queryset:QuerySet):
      queryset.update(auction = False)


   @admin.action(description='Добавить возможность торга')
   def make_auction_as_true(self,request,queryset:QuerySet):
      queryset.update(auction = True)   
 






# подключаю модель
admin.site.register(Advertisement, AdvertisementAdmin)



# admin.site.register(Test)

# py manage.py createsuperuser - создание аккаунта админа
# (вводин имя почту и пароль   ! пароль не отображается )
# http://127.0.0.1:8000/admin