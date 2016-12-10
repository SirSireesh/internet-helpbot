from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from watson_developer_cloud import ConversationV1
import os
from . import get_step

# Create your views here.

class message(APIView):

    def get(self, request, *args, **kw):
        msg = request.GET.get('message', None)
        contextstr = request.GET.get('context', None)
        contextjson = json.loads(contextstr)
        workspace_id = os.environ['IBMWID']
        conversation = ConversationV1(
                  username=os.environ['IBMUNAME'],
                  password=os.environ['IBMPASS'],
                  version='2016-09-20'
        )
        response = conversation.message(
                workspace_id=workspace_id,
                message_input={'text': msg},
                context=contextjson
        )
        print(response['entities'][0]['value'])
        result = Response(response, status=status.HTTP_200_OK)
        return result
