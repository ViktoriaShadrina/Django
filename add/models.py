from django.db import models
from django.contrib import admin
from django.utils import timezone # для времени
from django.utils.html import format_html # для создания строки html 
# venv/Scripts/activate
# название цена описание дата создания/обновления   торг

# py manage.py makemigrations - создание файлов миграции
# py manage.py migrate - выполнение миграций (создание физических таблиц)

class Advertisement(models.Model):# наследую класс Model для создания таблицы в БД
    title = models.CharField('название',max_length=100) #  текстовое поле
    description = models.TextField("описание")
    price = models.DecimalField('цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text='Отметьте, возможен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)# сохраняем дату создания
    updated_at = models.DateTimeField(auto_now=True)# дата будет обновляться каждый раз при измении обьявления


    # представление в виде строки 
    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    #работы с самой таблицей
    class Meta:
        db_table = 'add' # название таблицы

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date(): # проверяю что запись была создана сегодня
            created_time =  self.created_at.time().strftime("%H:%M:%S") # делаю в формате %H:%M:%S (12:20:30)
            return format_html(
                '<span style = "color:green; font-weight:bold">Сегодня в {}</span>',created_time
            )
        return self.created_at.strftime("%d.%m.%Y at %H:%M:%S")



    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date(): # проверяю что запись была создана сегодня
            updated_time =  self.updated_at.time().strftime("%H:%M:%S") # делаю в формате %H:%M:%S (12:20:30)
            return format_html(
                '<span style = "color:green; font-weight:bold">Сегодня в {}</span>',updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y at %H:%M:%S")




















# py manage.py shell
# from add.models import Advertisement
# adv1 = Advertisement(title = 'Дошик', description = 'Дошик с помидором', price=26, auction = True) # создал запись
# adv1.save()  # сохраняю запись

# Advertisement.objects.all()



# from django.db import connection
# connection.queries # увидеть все запросы на sql


#exit()




class Test(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)





class User(models.Model):



    GENDER_CHOICE = [
        ('Орк','Орк'),
        ('Фурри','Фурри'),
        ('Spider man','Spider man'),
    ]


    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(
        choices=GENDER_CHOICE,
        max_length=50,
        default='Орк'
    )
    mail  = models.EmailField()



































