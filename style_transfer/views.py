import os
import time

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from style_transfer.forms import UploadContentForm
from style_transfer.models import Style


def home(request):
    content = None
    styles = Style.objects
    if request.method == 'POST' and request.FILES['content']:
        content = request.FILES['content']
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 
                                                    'content'))
        fs.save(content.name,content)
        print(content.name)
    return render(request, 'style_transfer/index.html', {'content':content , 'styles':styles})
