from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)

    def create_pairs(self):
        all_persons = Person.objects.all()
        for person in all_persons:
            pair = Pair(pair1 = self, pair2 = person, count = 0 )
            pair.save()


class Pair(models.Model):
    pair1 = models.ForeignKey(Person, related_name='pair2')
    pair2 = models.ForeignKey(Person, related_name='pair1')
    count = models.IntegerField()


    def add_count_to_pair(self):
        self.count +=1


            
        


    
