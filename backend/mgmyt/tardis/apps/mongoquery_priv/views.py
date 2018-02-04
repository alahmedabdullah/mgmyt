from exceptions import TypeError, SyntaxError, ValueError
from tardis.apps.mongoquery.models import Collection, UserCollection, Job
from tardis.apps.mongoquery.api.serializers import CollectionSerializer, JobSerializer
from tardis.apps.mongoquery.forms import QueryForm
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer,BrowsableAPIRenderer
from django.shortcuts import get_object_or_404
import json

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from tardis.tardis_portal.auth import decorators as authz
from tardis.tardis_portal.models import \
    Experiment, Schema
from tardis.tardis_portal.shortcuts import render_response_index, \
    return_response_error, return_response_not_found, \
    RestfulExperimentParameterSet

import logging
logger = logging.getLogger(__name__)
print __name__

#@authz.experiment_access_required
def index(request, experiment_id):
    logger.debug('aaa %s' % experiment_id)
    try:
        experiment = Experiment.safe.get(request.user, experiment_id)
    except PermissionDenied:
        return return_response_error(request)
    except Experiment.DoesNotExist:
        return return_response_not_found(request)

    logger.debug('%s' % experiment)
    c = {'experiment': experiment}
    logger.debug('%s' % c)

    template = 'mongoquery/index.html'
    logger.debug('%s' % template)
    return HttpResponse(render_response_index(request, template, c))
