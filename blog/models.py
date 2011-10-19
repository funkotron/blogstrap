from django.conf import settings
from django.db import models
from datetime import datetime
import markdown, re

pattern = r'(https?://[-A-Za-z0-9+&@#%?=~_()|!:,.;]*[-A-Za-z0-9+&@#%=~_()|])(/.*)'
domain = re.compile(pattern)

class Social(models.Model):
    url = models.URLField()
    label = models.CharField(max_length=255)

    def favicon(self):
        return domain.match(self.url).groups()[0]+ "/favicon.ico"
    
    def __unicode__( self ):
        return self.url

class Tag(models.Model):
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=10,choices=(('default','Default'),('success','Success'),('warning','Warning'),('important','Important'),('notice','Notice')),default='default')

    def __unicode__( self ):
        return self.name

class Image(models.Model):
    name = models.CharField( max_length=100 )
    image = models.ImageField( upload_to="image" )

    def __unicode__( self ):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    body = models.TextField()
    datetime = models.DateTimeField(default=datetime.now())
    tags = models.ManyToManyField(Tag,blank=True,null=True)
    images = models.ManyToManyField(Image,blank=True,null=True)
    page = models.BooleanField(default=False)

    #TODO override save for slug
    
    def render_body(self):
        md = markdown.Markdown()

        for image in self.images.all():
            image_url = settings.MEDIA_URL + image.image.url
            md.reference[image.name] = (image_url, '')

        return md.convert(self.body)

    def __unicode__( self ):
        return self.name
