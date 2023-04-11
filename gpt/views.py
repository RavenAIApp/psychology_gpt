import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

from .models import Doctor, Patient, Record
from .process import ProcessRecord

# Create your views here.

class PsyGPTView(generic.View):

    # Post function to handle Facebook messages
    # @csrf_exempt
    def post(self, request, *args, **kwargs):

        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        print(incoming_message)
        
        # get userinfo
        user_name = incoming_message["text"]["user"]
        process = ProcessRecord(user_name)

        # get msg from request
        msg = incoming_message["text"]["info"]
        print(user_name)
        print(msg)
        result = process.getReply(msg)
        print(result)
        return HttpResponse(result)
