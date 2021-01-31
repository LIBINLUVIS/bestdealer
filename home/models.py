from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class image(models.Model):
    
    img = models.ImageField(upload_to='pics', null=True, blank=True)
    name = models.TextField(max_length=100)
    pro_type = models.TextField(max_length=250)
    pro_con=models.TextField(max_length=100)
    pro_Loc=models.TextField(max_length=200)
    pro_price=models.IntegerField()
    likes=models.ManyToManyField(User,related_name="pro_likes")
    auther=models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name='post_likes')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    latitude=models.FloatField(blank=True,null=True)
    logitude=models.FloatField(blank=True,null=True)
   

    def __str__(self):
        return self.name

    def total_likes(self):
        return self.likes.count()
       

    
class comment(models.Model):
    message=models.TextField(max_length=100)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    replay=models.ForeignKey('comment',null=True,related_name='replies',on_delete=models.CASCADE)
    product=models.ForeignKey(image,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)


class userprofile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to='pics',null=True,blank=True)
   
class userphone(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    phone=models.TextField(max_length=50,null=True,blank=True)


    
#userprofile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	
	if created:
		userprofile.objects.create(user=instance)
		print('Profile created!')

post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
	
	if created == False:
		instance.userprofile.save()
		print('Profile updated!')

post_save.connect(update_profile, sender=User)
