from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site

try:
    url = '/cookies'
    try:
        FlatPage.objects.get(url=url)
    except FlatPage.DoesNotExist:
        fp = FlatPage.objects.create(url=url, title='Cookie Policy', content='@todo')
        fp.sites.add(Site.objects.get(id=1))
except:
    pass
