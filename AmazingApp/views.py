# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from django.shortcuts import render, redirect
from django.db.models import Q
from django.db.models import F
from django.http import HttpResponse
from datetime import datetime, time



def index(request):
    return render(request, 'RolesManage/home.html',{"index":"active"})  #主页
def chat(request):
    return render(request,'RolesManage/TalkChat.html',{"index":"active"})#
def reconder(request):
    return render(request,'RolesManage/Reconder.html')

def knowledgebase(request):
    return render(request,'RolesManage/KnowledgeBase.html',{"KnowledgeBase":"active"})#知识库

def notice(request):
    return render(request,'RolesManage/Notice.html',{"Notice":"active"})#公告  Issue Report

def issuereport(request):
    return render(request,'RolesManage/IssueReport.html ',{"IssueReport":"active"})#问题上报

def issuefeedback(request):
    return render(request,'RolesManage/IssueFeedback.html',{"issuefeedback":"active"})#问题反馈