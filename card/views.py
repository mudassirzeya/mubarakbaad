from django.shortcuts import render, redirect
from .forms import Createform
from .models import Create_card
import random
import string
# from wishing import settings
# import os
# from PIL import Image
# from django.core.files.base import File
# Create your views here.


def wishing_card(request, pk=''):
    if pk == '':
        context = {}
        return render(request, 'card/wishing.html/', context)
    else:
        user = Create_card.objects.filter(random_str=pk).first()
        context = {'user': user}
        return render(request, 'card/wishing.html/', context)


def create_card(request):
    form = Createform()
    random_string = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(8))
    if request.method == 'POST':
        print("request.POST: ", request.POST)
        userform = Createform(request.POST, request.FILES)
        if userform.is_valid():
            print("form valid")
            userObj = userform.save(commit=False)
            userObj.random_str = random_string
            print('user_pic', userObj.profile_pic)
            userObj.save()
            # media_url = userObj.profile_pic.url
            # print('media: ', media_url)
            # print('basedir: ', settings.BASE_DIR)
            # media_join = os.path.join(settings.BASE_DIR, media_url[1:])
            # print('media_join: ', media_join)
            # im = Image.open(media_join)
            # im.save("img_4_compressed.jpg", format="JPEG", quality=60)
            # print('im: ', im)

            # # Using File
            # with open('/path/to/file') as f:
            #     self.license_file.save(userObj.profile_pic, File(f))

            return redirect('wishing', pk=userObj.random_str)
        else:
            print("form not valid")
        return redirect('create')
    context = {'form': form}
    return render(request, 'card/create.html/', context)
