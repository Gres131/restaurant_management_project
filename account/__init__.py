from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.permission import IsAuthenticated
from rest_framework.authtoken.models import Token 
from rest_framework.authtoken.views import obtain_auth_token
from django.db.models.signals import post_save
from django.dispatch import receiver

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['owner']


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serialize.save(owner=self.request.user)

@receiver(post_save, sender=User)
def create_user_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token.objects.create(user=instance)
    

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSSES':[
        'rest_framework.authentication.TokenAuthentication'
    ],
}