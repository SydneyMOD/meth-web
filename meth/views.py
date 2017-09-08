import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')

def index(request):
    context = {}
    template = 'index.html'
    return render(request, template, context)


def docs(request, page='index'):
	STATUS_CODE = 200
	if not os.path.isfile(f'{TEMPLATES_DIR}/docs/{page}.md'):
		page = '404'
		STATUS_CODE = 404

	md = open(f'{TEMPLATES_DIR}/docs/{page}.md').read()

	context = {'markdown_string': md, 'file_name': page, 'docs': docs}
	template = 'docs.html'
	return render(request, template, context, status=STATUS_CODE)


def download(request):
	context = {}
	template = 'download.html'
	return render(request, template, context)


def package(request):
	context = {}
	template = 'package.html'
	return render(request, template, context)
