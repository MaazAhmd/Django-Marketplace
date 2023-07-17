from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import messageForm
from .models import Conversation, Message
from website.models import Item

# Create your views here.

def conversation(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    conversations = Conversation.objects.filter(members__in = [request.user.id]).filter(item=item)

    if conversations:
        return redirect('inbox')

    if request.method=='POST':
        form = messageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()
            return redirect('index')

    else:
        form = messageForm()

    return render(request, 'conversation/messages.html', {
        'form': form,
        'item': item
    })

def inbox(request):
    conversations = Conversation.objects.filter(members__in = [request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

def chat(request, pk):
    # item = Item.objects.get(pk=item_pk)
    conversation = Conversation.objects.filter(members__in = [request.user.id]).get(pk=pk)
    messages = Message.objects.filter(conversation=conversation)

    if request.method=='POST':
        form = messageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.conversation = conversation
            msg.created_by = request.user
            msg.save()
    else:
        form = messageForm()

    return render(request, 'conversation/chat.html', {
        'conversation': conversation,
        'messages': messages,
        'form': form,
    })
