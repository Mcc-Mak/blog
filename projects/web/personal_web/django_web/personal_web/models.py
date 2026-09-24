from django.db import models

# Create your models here.
class Model(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length= 50,help_text="e.g It is a happy day that I go to .......")
    content = models.TextField(max_length = 255)
    img = models.ImageField(default='',upload_to ='uploads/',null=True, blank=True, max_length=1000)


    class Meta:
        ordering  = ['-datetime']
        verbose_name_plural = "entries"
        
    # def get_absolute_url(self):
    #     return reverse('model-detail-view',args=[str(self.id)])

    def __str__(self):
        return "Entry #{}".format(self.title)




