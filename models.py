from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models import permalink
from django.contrib.auth.models import User

import datetime
import dateutil

class Person(models.Model):
    """Person model."""
    first_name   = models.CharField(_('first name'), blank=True, max_length=100)
    middle_name  = models.CharField(_('middle name'), blank=True, max_length=100)
    last_name    = models.CharField(_('last name'), blank=True, max_length=100)
    slug         = models.SlugField(_('slug'), unique=True)
    user         = models.ForeignKey(User, blank=True, null=True)
    photo        = models.ImageField(_('photo'), upload_to='photos',
                                        blank=True, null=True)
    photo_credit = models.CharField(_('photo credit'), blank=True, max_length=200)
    role         = models.ForeignKey('Role', unique=True)
    bio          = models.TextField(blank=True)
    website      = models.URLField(_('website'), blank=True, verify_exists=True)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')
        db_table = 'people'
        ordering = ('last_name', 'first_name',)

    def __unicode__(self):
        return u'%s' % self.full_name

    @property
    def full_name(self):
        if self.middle_name:
            return u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)
        else:
            return u'%s %s' % (self.first_name, self.last_name)

    @permalink
    def get_absolute_url(self):
        return ('person_detail', None, {'slug': self.slug})

class Role(models.Model):
    ACTING = 0
    PRODUCING = 1
    MARKETING = 2
    DESIGNING = 3
    BUILDING = 4
    DIRECTING = 5
    PRODUCTION_MANAGING = 6
    TYPE_CHOICES = (
        (ACTING, "Acting"),
        (PRODUCING, "Producing"),
        (MARKETING, "Marketing"),
        (DESIGNING, "Designing"),
        (BUILDING, "Building") ,
        (DIRECTING, "Directing"),
        (PRODUCTION_MANAGING, "Production Managing")
    )

    type = models.IntegerField(_('type'), choices=TYPE_CHOICES)
    position = models.CharField(_('position'), max_length=40)
    description = models.TextField(_('description'), blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.get_type_display(), self.position)
