import json

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import ChatConversation, ChatMessage
from .functions import limit_number
from contact.models import ChatUser
from .functions import serialize_foreign_key


# Create your views here.
def index(request):
    chats = ChatConversation.objects.all()
    return render(request, 'chat/index.html', {'chats': chats})


# TODO: Create Restful API views.
# def all_conversations_from_admin_app(request):


def conversations_from_user(request, admin_app_uuid, user_uuid):
    limit = limit_number(request.GET.get('limit'))

    # Worth it to search also for which app (hotelflow, or other site) uuid the message is from? Or just the single
    # uuid author search make the performance better?
    #        .order_by('created')[-limit_number]
    # There's not a way that a conversation can be without users from both sides. An operator must send a message
    # to a registered/non-registered user, and a registered/non-registered user must send a message to an operator.
    # If there's no operator assigned, assign a random one, or a default one (should be a bot?).
    # We query with uuid when we have the uuid in the request. Therefore, we query with the whole object?
    conversations_queryset = ChatConversation.objects.filter(message_app__uuid=admin_app_uuid, customer__uuid=user_uuid)

    if limit > 0:
        conversations_queryset = conversations_queryset[-limit]

    print('opa', conversations_queryset.values_list('pk', flat=True))

    return HttpResponse(json.dumps(list(conversations_queryset.values()), default=str), content_type='application/json')


# def all_messages_from_admin_app(request):
#     messages = list(
#     ChatMessage.objects.all().values('id', 'message', 'message_author', 'editable', 'deletable', 'created', 'uuid'))
#     return JsonResponse(messages, safe=False)

def conversation(request, admin_app_uuid, conversation_uuid):
    # TODO: GET SOME THINGS FROM THE USER SESSION.
    # TODO: MAKE SESSION ID (CLIENT SIDE?).
    message_limit = limit_number(request.GET.get('limit'))

    conversation = ChatConversation.objects.get(
        message_app__uuid=admin_app_uuid,
        uuid=conversation_uuid
    )

    conversation_messages = conversation.messages

    # If there's a message limit, then slice the conversation messages to return.
    if message_limit > 0:
        conversation_messages = conversation_messages[-message_limit]

    # Transform the messages list in a python list with the required values.
    messages_list = list(conversation_messages.values(
        'message', 'message_author__uuid', 'message_status', 'message_channel', 'reopen_time',
        'editable', 'deletable', 'created', 'updated', 'uuid'
    ))

    # Iterate over the messages list. If it was only one message instead of a list, the for loop would be not necessary.
    for message in messages_list:
        find_author_query = {
            'uuid': message['message_author__uuid']
        }
        # WARNING: Mutates the message object.
        serialize_foreign_key(
            message, ChatUser, 'message_author', **find_author_query
        )
        # # Get the author of the current message.
        # message_author = ChatUser.objects.get(uuid=message['message_author__uuid'])
        #
        # # Initialize the author holder info.
        # message['message_author'] = {}
        #
        # # Remove the author uuid key from the object.
        # message.pop('message_author__uuid')
        #
        # # Build the message_author information.
        # for key, value in model_to_dict(message_author).items():
        #     message['message_author'][key] = value

    # Eduardo itera assim mesmo sobre as foreign keys (reservas, quartos, channel manager por exemplo)
    # for item in messages_list:
    #     print('item', item)

    data = {
        'id': conversation.id,
        'uuid': str(conversation.uuid),
        'messages': messages_list,
        'operator': {
            'username': conversation.operator.username,
            'uuid': conversation.operator.uuid,
        },
        'customer': {
            'username': conversation.customer.username,
            'uuid': conversation.customer.uuid
        },
        'created': 'created',
        'last_message': 'last message'
    }

    return HttpResponse(json.dumps(data,default=str), content_type='application/json')


def messages_from_user(request, admin_app_uuid, user_uuid):
    limit = limit_number(request.GET.get('limit'))

    messages_queryset = ChatMessage.objects.filter(
        chatconversation__message_app__uuid=admin_app_uuid,
        message_author__uuid=user_uuid
    )

    if limit > 0:
        messages_queryset = messages_queryset[-limit]

    messages = list(messages_queryset.values())

    return JsonResponse(messages, safe=False)


def room(request, room_name):
    return HttpResponse(json.dumps({
        'room_name': 'one_room'
    }), content_type='application/json')
    # return render(request, 'chat/room.html', {
    #     # 'room_name_json': mark_safe(json.dumps(room_name))
    #     'room_name_json': 'one_room'
    # })
