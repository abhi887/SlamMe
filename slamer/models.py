from django.db import models

class user(models.Model):
    username=models.CharField(max_length=40,primary_key=True)
    name=models.CharField(max_length=30)
    bio=models.CharField(max_length=150,null=True)

    def __str__(self):
        return(f"username : {self.username} | name : {self.name}")

class abs_user(models.Model):
    uid=models.ForeignKey('user',on_delete=models.CASCADE)
    key=models.CharField(max_length=20)
    logged=models.BooleanField(null=True)

    def __str__(self):
        return(f"username : {self.uid.username} | key : {self.key} | logged = {self.logged}")

class slam_request(models.Model):
    req_from=models.CharField(max_length=40)
    req_to=models.CharField(max_length=40)

    def __str__(self):
        return(f"{self.id} | {self.req_from} -> {self.req_to} |")

class slam_post(models.Model):
    post_from=models.CharField(max_length=40)
    post_for=models.CharField(max_length=40)
    public=models.BooleanField(null=True)
    f1=models.CharField(max_length=400,null=True)
    f2=models.CharField(max_length=400,null=True)
    f3=models.CharField(max_length=400,null=True)
    f4=models.CharField(max_length=400,null=True)
    f5=models.CharField(max_length=400,null=True)
    f6=models.CharField(max_length=400,null=True)
    f7=models.CharField(max_length=400,null=True)
    f8=models.CharField(max_length=400,null=True)
    f9=models.CharField(max_length=400,null=True)
    f10=models.CharField(max_length=400,null=True)
    f11=models.CharField(max_length=400,null=True)
    f12=models.CharField(max_length=400,null=True)
    f13=models.CharField(max_length=400,null=True)
    f14=models.CharField(max_length=400,null=True)
    f15=models.CharField(max_length=400,null=True)
    f16=models.CharField(max_length=400,null=True)

    def __str__(self):
        return(f"from: {self.post_from} -> to: {self.post_for} | public: {self.public}")