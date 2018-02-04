from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)
print __name__

def index(request, experiment_id):
    logger.debug('%s' % experiment_id)

    logger.debug('%s' % experiment_id)
    c = {'experiment': experiment_id}
    logger.debug('%s' % c)

    template = loader.get_template('mongoquery/index_local.html')
    logger.debug('%s' % template)
    return HttpResponse(template.render(c,request))
