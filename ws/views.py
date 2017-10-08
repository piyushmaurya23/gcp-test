# -*- coding: utf-8 -*-
"""
This module is a standard Django generated views module for custom application
"""
import json
# Create your views here.
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from ws.models import User, Domain


def account_is_licensed(request):
    """Function check is this account is licensed or not.

       Returns:
           HttpResponse: Full http response from server.
    """
    email = request.GET['email']
    version = request.GET['version']

    # Validating email
    try:
        validate_email(email)
    except ValidationError:
        return HttpResponse("Email address is invalid")

    user_name = email.split("@")[0]
    domain_name = email.split("@")[1]
    # checking user is licensed
    try:
        user = User.objects.get(name=user_name)
        user_licensed = user.is_licensed
    except ObjectDoesNotExist:
        user_licensed = False

    # checking domain is licensed
    try:
        domain = Domain.objects.get(name=domain_name)
        domain_licensed = domain.is_licensed
    except ObjectDoesNotExist:
        domain_licensed = False

    licensed = True if user_licensed and domain_licensed else False

    # validating version
    version_updated = version == settings.VERSION

    response = json.dumps(dict(license=licensed, updated=version_updated), sort_keys=True)
    return HttpResponse(response)
