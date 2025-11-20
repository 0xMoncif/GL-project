
# ****** i'll think more so i can implement this correctly, now i'm i bit confused *****

# from django.db import models

# class Notification(models.Model):
#     user=models.ForeignKey('profiles.StudentProfile', on_delete=models.CASCADE)
#     offer=models.ForeignKey('offers.Offer', on_delete=models.CASCADE)
# #   condidature= models.ForeignKey('', on_delete=models.CASCADE)   
#     title=models.CharField(max_length=25)
#     mssg=models.TextField()
#     Notification_Types= [
        
#     ]
#     type= models.CharField(max_length=50, choices=Notification_Types, )
#     created_at= models.DateField(auto_now=True)
#     is_read= models.BooleanField(default=False)
# #     offer=models.ManyToManyField('offers.offer', through='notifications.offerNotification' )


# # class offerNotification (models.Model):
# #     notification=models.ForeignKey(Notification,on_delete=models.CASCADE, related_name='notifications')
# #     offer= models.ForeignKey('offers.Offer', on_delete=models.CASCADE, related_name='notificationOffers')

     
