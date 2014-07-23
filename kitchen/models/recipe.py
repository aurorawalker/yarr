from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

CATEGORIES = (
              ('breakfast', _('Breakfast')),
               ('lunch', _('Lunch')),
               ('dinner', _('Dinner')),
               ('dessert', _('Dessert')),
               ('witchcraft', _('Witchcraft')),
            )


class Recipe(models.Model):
    user = models.ForeignKey(User, related_name='owner', help_text="The user who created this recipe." )
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Summary/Abstract")
    ingredients = models.TextField(help_text="The ingredients and their amounts")
    steps = models.TextField(help_text="The recipe instructions")# The actual method of creating the recipe
    notes = models.TextField(help_text="Additional notes/variants")
    category = models.CharField(null=True, blank=True, max_length=30, choices=CATEGORIES, help_text="The category type of the recipe.")
    # tags = # some kind of additonal list? (season, etc. search terms)
    source = models.CharField(max_length=1000, null=True, blank=True, help_text="Where this recipe came from")
    # time = # how long it takes to do
    #image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, help_text=_('Date Created'))
    modified_at = models.DateTimeField(auto_now=True, help_text=_('Last Modified'))
    modified_by = models.ForeignKey(User, related_name='modifier', null=True, blank=True, help_text="The user who last updated or modified this recipe." )
    
    
    def __unicode__(self):
        return unicode(self.title)
    
    class Meta:
        app_label='kitchen'
        ordering = ['created_at']
        