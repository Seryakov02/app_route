from django.db import models


class Bus(models.Model):
    number = models.IntegerField("Номер автобуса")
    image = models.ImageField("Изображение", upload_to="buses/")
    number_of_places = models.PositiveSmallIntegerField("Число мест", default=0)
    driver = models.CharField(max_length=255, verbose_name="Имя водителя")
    bus_brand = models.CharField(max_length=255, verbose_name="Марка автобуса")
    slug = models.SlugField(verbose_name="url", unique=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'


class Race(models.Model):
    bus = models.ForeignKey(Bus, verbose_name="Номер автобуса", on_delete=models.CASCADE)
    first_point_of_departure = models.CharField(max_length=255, verbose_name='Первый пункт отправления')
    first_shedule = models.TextField("Расписание")
    second_point_of_departure = models.CharField(max_length=255, verbose_name='Второй пункт отправления')
    second_shedule = models.TextField("Расписание")
    route = models.TextField("Маршрут следования")
    ticket_price = models.CharField(max_length=255, verbose_name='Цена билета')
    slug = models.SlugField(verbose_name="url", unique=True)

    def __str__(self):
        return f"Рейс {str(self.bus.number)} автобуса"

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'


class Suburban(models.Model):
    starting_point = models.CharField(max_length=255, verbose_name="Начальный пункт")
    terminus = models.CharField(max_length=255, verbose_name="Конечный пункт")
    departure_time = models.TextField("Время отправления")

    def __str__(self):
        return f"{str(self.starting_point)} - {str(self.terminus)}"

    class Meta:
        verbose_name = 'Электричка'
        verbose_name_plural = 'Электрички'
