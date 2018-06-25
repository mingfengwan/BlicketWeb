# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from polls.models import Participant
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


def index(request):
    item = Participant.objects.all()  # use filter() when you have sth to filter ;)
    form = request.POST  # you seem to misinterpret the use of form from django and POST data. you should take a look at [Django with forms][1]
    # you can remove the preview assignment (form =request.POST)
    if request.method == 'POST':
        selected_item = get_object_or_404(Participant, pk=request.POST.get('item_id'))
        # get the user you want (connect for example) in the var "user"
        # user.item = selected_item
        # user.save()

        # Then, do a redirect for example

    return render(request, 'index.html', {'items': item})


class ParticipantCreate(CreateView):
    model = Participant
    fields = '__all__'
    initial={'date_of_creation':'05/01/2018',}


class ParticipantUpdate(UpdateView):
    model = Participant
    fields = ['first_name','last_name','date_of_birth','date_of_death']


class ParticipantDelete(DeleteView):
    model = Participant
    success_url = reverse_lazy('participants')