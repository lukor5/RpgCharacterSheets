from django.db import models
from django.forms import ModelForm
from django.conf import settings
from PIL import Image

class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    class_level = models.CharField(max_length=20)
    race = models.CharField(max_length=15)
    background = models.CharField(max_length=15)
    alignment = models.CharField(max_length=20)
    player_name = models.CharField(max_length=20)
    xp = models.IntegerField()
    str = models.IntegerField()
    dex = models.IntegerField()
    con = models.IntegerField()
    int = models.IntegerField()
    wis = models.IntegerField()
    cha = models.IntegerField()
    str_save = models.IntegerField()
    dex_save = models.IntegerField()
    con_save = models.IntegerField()
    int_save = models.IntegerField()
    wis_save = models.IntegerField()
    cha_save = models.IntegerField()
    ac = models.IntegerField()
    init = models.IntegerField()
    speed = models.IntegerField()
    hp = models.CharField(max_length=9)
    hp_temp = models.IntegerField()
    portrait = models.ImageField(blank=True)
    
    def save(self):
        super().save()
        port = Image.open(self.portrait.path)
        if port.height > 100 or port.width > 100:
            new_port = (100, 100)
            port.thumbnail(new_port)
            port.save(self.portrait.path)
    
class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['user', 'name', 'class_level', 'race', 'background', 'alignment', 'player_name', 'xp', 'str', 'dex', 'con',
                  'int', 'wis', 'cha', 'str_save', 'dex_save', 'con_save', 'int_save', 'wis_save', 'cha_save', 'ac', 'init',
                  'speed', 'hp', 'hp_temp', 'portrait']
    
    
