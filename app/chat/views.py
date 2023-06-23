from django.shortcuts import render
from django.views.generic import TemplateView
import time
import random
from .models import User, Message

# Create your views here.
class ChatView(TemplateView):
    template_name = "chat.html"


    def get(self,request):
        # store user_id in cookie
        user_id = request.COOKIES.get('user_id')
        if not user_id:
            # Generate a unique identifier
            user_id = generate_user_id()  # Implement your own logic to generate a unique user ID

            # Set the unique identifier in a cookie
            request.set_cookie('user_id', user_id)
           
        

        # retrieve messages
        messages = Message.objects.filter(user_id=user_id)
        
        return render(request, self.template_name, {'Messages': messages})


    def post(self, request):
        # get user_id from session or generate new one 0
        user_id = request.COOKIES.get('user_id')
        # import ipdb;ipdb.set_trace()
        message = request.POST.get("message")

        # save message to database
        user = User.objects.get(user_id=user_id)
        
        message_instance = Message(user_id=user, message=message)
        message_instance.save()

        return render(request, self.template_name)
    

def generate_user_id():
    timestamp = str(int(time.time() * 1000))  # Convert current timestamp to milliseconds
    random_num = str(random.randint(0, 9999)).zfill(4)  # Generate a random number padded with zeros
    user_id = timestamp + random_num
    
    User_instance = User(user_id=user_id)
    User_instance.save()

    return user_id