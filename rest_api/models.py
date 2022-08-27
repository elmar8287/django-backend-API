from django.db import models

class Cars(models.Model):
  name    = models.CharField(max_length=100)
  number  = models.CharField(max_length=100)
  company = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Cars'

class Days(models.Model):
  name         = models.CharField(max_length=100)
  note         = models.TextField()

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Days'

class Booking(models.Model):
  name         = models.CharField(max_length=100)
  day          = models.ForeignKey(Days, on_delete=models.CASCADE)
  car          = models.ForeignKey(Cars, on_delete=models.CASCADE)

  def __str__(self):
    return self.name