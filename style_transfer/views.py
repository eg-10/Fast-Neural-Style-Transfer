import os
import time
from PIL import Image

from django.core.files.images import ImageFile
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse

from style_transfer.forms import UploadContentForm
from style_transfer.models import Style

from stylize import stylize


def home(request):
    content = None
    styles = Style.objects
    if request.method == 'POST' and request.FILES['content']:
        content = request.FILES['content']
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 
                                                     'content'))
        filename = fs.save(content.name,content)
        img_path = os.path.join(fs.location, filename)
    return render(request, 'style_transfer/index.html', {'content':content , 
                                                         'styles':styles})

def apply_style_transfer(request):
    if (request.method == 'GET' and request.GET['style_id'] 
                                and request.GET['img_name']):
        style = get_object_or_404(Style, pk=request.GET['style_id'])
        model_path = os.path.join(settings.MEDIA_ROOT, style.model.name)
        img_path = os.path.join(settings.MEDIA_ROOT, 'content', request.GET['img_name'])
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 
                                                     'results'))
        result = stylize.style(img_path, model_path)
        filename = 'result_' + str(int(time.time())) + '.jpg'
        result.save(os.path.join(settings.MEDIA_ROOT, 'results', filename))
        print('just made '+filename)
        return HttpResponse('/media/results/' + filename)

