from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserApi(models.Model):
    email = models.CharField(max_length=300)
    wazirApi = models.CharField(max_length=300, blank = True)  
    wazirSecret = models.CharField(max_length=300, blank = True)  
    binanceApi = models.CharField(max_length=300, blank = True)  
    binanceSecret = models.CharField(max_length=300, blank = True)  
    ftxApi = models.CharField(max_length=300, blank = True)  
    ftxSecret = models.CharField(max_length=300, blank = True)  
    uniswapPublic = models.CharField(max_length=300, blank = True)  
    uniswapPrivate = models.CharField(max_length=300, blank = True)  
    