from django.shortcuts import render

# Create your views here.

class PsyGPTView(generic.View):

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):

        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))

        # get userinfo

        # get msg from request

        # insert patient db

        # form prompt 

        # gpt qa

        # insert gpt answer into db

        return HttpResponse()
