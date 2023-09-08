import csv
import datetime


from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from page_5.models import GameModel, GamerLibraryModel, GamerModel


def upload_data(request):
    with open('vgsales.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
                _, created = GameModel.objects.get_or_create(
                    name=row[1],
                    platform=row[2],
                    year=datetime.date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],
                )
            except:
                pass
    return HttpResponse("Done!")


class FilterView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(
        Q(name__startswith="Ad") | ~Q(name__startswith="Ad") | Q(name__startswith="Mat"))


def relation_filter_view(request):
    data = GamerLibraryModel.objects.filter(gamer__email__contains="a")
    print(data[0].gamer.email)
    return HttpResponse(data.order_by("?"))



class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains="Hitman")


class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    # TODO add reverse
    queryset = GameModel.objects.exclude(name__contains="Hitman").order_by('year').reverse()



class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()



class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    # TODO add reverse
    queryset = GameModel.objects.filter(name="Hitman (2016)").union(GameModel.objects.filter(name="Tetris"))



class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()



class ValuesView(ListView):
    template_name = 'gamemodel_list.html'

    queryset = GameModel.objects.filter(name="Hitman (2016)").values()

    def get(self, request, *args, **kwargs):
        print(list(
            GameModel.objects.filter(name="Hitman (2016)").values_list("name", "platform")))
        return super().get(request, *args, **kwargs)



def date_view(request):
    data = GameModel.objects.dates(field_name="year", kind="month")
    print(data)
    return HttpResponse(data)



def get_view(request):
    # TODO try error
    data = GameModel.objects.get(pk=1)
    print(data)
    return HttpResponse(data)


def create_view(request):
     myself = GamerModel.objects.bulk_create([GameModel(email="admin@admin.com", nickname="SomeRandomNickname1"),
                                              GameModel(email="admin@admin.com", nickname="SomeRandomNickname2")])

     return HttpResponse(myself)


