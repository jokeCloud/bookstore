from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from stdimage.models import StdImageField


class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Product(Base):
    name = models.CharField('Product', max_length=100)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    stock = models.IntegerField('Stock')
    image = StdImageField('Image', upload_to='products',
                          variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name


def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(product_pre_save, sender=Product)
