import os
import json
import requests

from .models import Doctor, Patient, Record
from .utils.openai import OpenAIUtils

class ProcessRecord(object):

    prompt_template_start = \
    """
I need you to be a psychological counselor to talk to patients, provide as much support and encouragement as possible to make them feel comfortable and at ease before communicating with a real psychological counselor, and at the same time gather the following information, which will be reported to the artificial psychological counselor. \n

Here is the list of information to be obtained:\n
1. What is the reason for your visit?\n
2. Have you recently been troubled by anything specific?\n
3. How long have you been feeling troubled?\n
4. How much impact do you think this problem has on your daily life?\n
5. Have you sought help elsewhere?\n
6. Have you been diagnosed with any mental health problems?\n
7. How is your family and social life?\n
8. How is your work or study situation?\n
9. Do you have any other physical or mental illnesses?\n
10. What are your expectations or goals for psychological counseling?\n

The chat record that has been generated so far is as follows:\n
    """

    prompt_template_end = \
    """
Based on the above description and the patient's last statement in the chat record, please reply with your response. No prefix is necessary, only the content of your reply is required.
    """

    prompt_opening = "How may I help you?"

    def __init__(self, p_name):
        self.__patient_name = p_name
        self.__message = ""
        self.__prompt = ""
        self.__reply = ""
        self.__record_id = 0 

    def getPrompt(self):
        # get patient from db
        patient = Patient.objects.filter(Name = self.__patient_name)
        if len(patient) == 0:
            pAdd = Patient.objects.create(Name = self.__patient_name)
            rAdd  = Record.objects.create(PatientID = pAdd, Description = self.__message)
            self.__record_id  = rAdd.id
            msgs = "Patient: " + self.__message + "\n"
            print(self.__record_id)
            print(msgs)
            return ProcessRecord.prompt_template_start + msgs + ProcessRecord.prompt_template_end
        else:
            pinfo = Patient.objects.filter(Name = self.__patient_name)
            records = Record.objects.filter(PatientID = pinfo[0].id)
            msgs = ""
            for record in records:
                msgs += "Patient: "  + record.Description + "\n"
                msgs += "You: "  + record.Reply + "\n"
            msgs = "Patient: " + self.__message + "\n"
            print(msgs)
            return ProcessRecord.prompt_template_start + msgs + ProcessRecord.prompt_template_end

    def saveAnswer(self):
        Record.objects.filter(id=self.__record_id).update(Reply=self.__reply)

    def getReply(self, msg):
        self.__message = msg
        self.__prompt = self.getPrompt()
        self.__reply = OpenAIUtils.simple_answer(self.__prompt)
        self.saveAnswer()
        return self.__reply
