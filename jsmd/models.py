from django.db import models
import datetime


def get_today():
    t = datetime.datetime.now()
    return('%d-%d-%d' % (t.year, t.month, t.day))

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True, default='VIC')
    zip_code = models.SmallIntegerField(null=True)
    country = models.CharField(max_length=50, default='AUSTRALIA')
    phone_number = models.CharField(max_length=50, blank=True)
    company_website = models.URLField(blank=True)
    additional_notes = models.TextField(max_length=200, blank=True)


    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ['company_name']


class Contact(models.Model):
    personal_prefix = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    additional_notes = models.TextField(max_length=200, blank=True)


    def __str__(self):
        return u'%s %s %s' % (self.personal_prefix, self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']

    
class Application(models.Model):
    date_posted = models.DateField(default=get_today())
    date_applied = models.DateField(default=get_today())
    company = models.ForeignKey(Company)
    position_name = models.CharField(max_length=50)
    position_code = models.CharField(max_length=50, blank=True)
    contact = models.ForeignKey(Contact)
    place_advertised = models.CharField(max_length=50)
    interview = models.BooleanField(default=False)
    additional_notes = models.TextField(max_length=200, blank=True)
    resume = models.FileField(blank=True, null=True)
    cover_letter = models.FileField(blank=True, null=True)


    def __str__(self):
        return self.position_name

    class Meta:
        ordering = ['-id']
