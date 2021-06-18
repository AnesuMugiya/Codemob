import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Flame

@login_required
def api_add_flame(request):
     data = json.loads(request.body)
     user_id = data[user_id]

     if not Flame.objects.filter(user_id=user_id).filter(create_by =request.user).exists():
          flame = Flame.objects.create(user_id=user_id, created_by=request.user)

     return JsonResponse({'success': True})