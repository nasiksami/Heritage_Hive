from django.http import JsonResponse
from Category.models import Category
from subscribe.models import SubscribeModel
from account.models import Account
from subscribe.classes import ConcreteSubject
# Create your views here.
# this is to subcribe the subject to be observed by an observer
def subscribe(request,category_id):
   try:
       user=request.user
       if request.user.is_authenticated==False:
            return JsonResponse({'error':"Sign in first"},status=400)
       category=Category.objects.get(id=category_id)
       print(category)
       subscribed, created = SubscribeModel.objects.get_or_create(category=category)
       subject=ConcreteSubject()
       subject.register(subscribed,user)
       return JsonResponse({'message':"Category Subscribed"},status=200)

   except Exception as e:
        error=str(e)
        print(error)
        return JsonResponse({'error':f"unexcepcted error: {error}"},status=400)

# this is to unsubcribe the subject which was observed by an observer
def unsubscribe(request,category_id):
    try:
       user=request.user
       if request.user.is_authenticated==False:
            return JsonResponse({'error':"Sign in first"},status=400)

       category=Category.objects.get(id=category_id)
       subscribed = SubscribeModel.objects.get(category=category)
       subject=ConcreteSubject()
       subject.unregister(subscribed,user)
       return JsonResponse({'message':"Category Unsubscribed"},status=200)
    except Exception as e:
        error=str(e)
        print(error)
        return JsonResponse({'error':f"unexcepcted error: {error}"},status=400)

