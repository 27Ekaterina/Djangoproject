# Основные
# all, get, filter

# Открыть shell, ровести сначала импорт, затем писать запросы
# from blog.models import Video, Tag


# Video.objects.all()
# Video.objects.filter(pk=1)
# Video.objects.get(pk=1).title

# Фильтры
# 1) с одним параметром
# Video.objects.filter(title='Аврора')
# 2) exclude - фильтр наоборот
# Video.objects.exclude(title='Аврора')
# 3) фильтр c несколькими параметрами
# Video.objects.filter(title='Адмиралтейство', description='Адмиралтейство, Санкт-Петербург')
# 4) Можно применять любые запросы к полученному QuerySet
# >>> Admiralteystvo =  Video.objects.filter(title='Адмиралтейство')
# >>> some = Admiralteystvo.filter(description='Адмиралтейство, Санкт-Петербург')
# в одну строку
# Admiralteystvo =  Video.objects.filter(title='Адмиралтейство').filter(description='Адмиралтейство, Санкт-Петербург')
# Admiralteystvo =  Video.objects.filter(title='Адмиралтейство').exclude(description='Адмиралтейство, Санкт-Петербург')


# Сложные фильтры
# 1. больше меньше (все видео с рейтингом больше 3)
# Video.objects.filter(rating__gt=3)
# Video.objects.filter(rating__lt=3)
# больше или равно Video.objects.filter(rating__gte=3)
# меньше или равно Video.objects.filter(rating__lte=3)

# 2. С рейтингом 2 или 3
# Video.objects.filter(rating__lte=4, rating__gte=2)
# Video.objects.filter(rating__in=[3, 4])

# 3. Видео, начинающиеся на (title) Ад...
# Video.objects.filter(title__startswith='Ад')

# 4. Видео, в названии которых есть Ав, ... кура... с учетом регистра
# Video.objects.filter(title__contains='кура')

# Видео, в названии которых есть Ав, ... кура... без учета регистра
# Video.objects.filter(title__icontains='кура') (не работает с SQLite на кириллице
# Video.objects.filter(title__iregex='Кура')работает с кириллицей

# 5. Видео с датой создания меньше какой-то
# Способ 1
# Создать объект - фиксированную дату и сравнить с ней
# import datetime
# some_date =datetime.datetime(year=2023, month=2, day=15)
# Video.objects.filter(create__gt=some_date)
# можно через список и указать несколько дат
# Video.objects.filter(create__in=[some_date])
# Способ 2
# Прямое сравнение с датой создания
# Video.objects.filter(create__year=2022, create__day=15, create__month=2)

# Запросы к связанным моделям
# Задача 1: Получить Видео с тегом у которого название Аврора
# Вариант на Pithon
# tag = Tag.objects.get(name='Аврора')
# Video.objects.filter(tags=tag)
# Вариант на orm
# Video.objects.filter(tags__name='Аврора')

# Задача 2: Получить Видео с тегом у которого название начинается на Ав
# Video.objects.filter(tags__name__startswith='Ав')

