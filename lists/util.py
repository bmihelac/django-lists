from django.contrib.auth.models import AnonymousUser

from .models import Folder

FOLDERS_SESSION_VARIABLE = 'folders'


def get_folder_from_session(session, folder_name):
    folders = session.get(FOLDERS_SESSION_VARIABLE)
    if not folders:
        return None
    folder_id = folders.get(folder_name)
    if not folder_id:
        return None
    folder = Folder.objects.get(pk=folder_id)
    return folder


def add_folder_to_session(request, folder):
    if not hasattr(request.session, FOLDERS_SESSION_VARIABLE):
        request.session[FOLDERS_SESSION_VARIABLE] = {}
    request.session[FOLDERS_SESSION_VARIABLE][folder.name] = folder.pk


def get_folder_from_request(request, folder_name, create=False):
    """
    Gets ``Folder`` named ``folder_name`` from request or initialize
    new ``Folder``.

    ``Folder`` is recieved from database for logged in users or
    from session for anonymous user.
    """
    is_logged_in = request.user and not isinstance(request.user, AnonymousUser)

    if is_logged_in:
        try:
            folder = Folder.objects.get(name=folder_name)
        except Folder.DoesNotExist:
            folder = Folder(user=request.user, name=folder_name)
    else:
        folder = get_folder_from_session(request.session, folder_name)
        if not folder:
            folder = Folder(name=folder_name)
    if not folder.pk and create:
        folder.save()
        if not folder.user:
            add_folder_to_session(request, folder)

    return folder


def add_item_to_folder(request, folder_name, obj):
    """
    Adds ``obj`` to ``folder`` with name ``folder_name`` for current request.

    If folder does not exists, it will be created.
    """
    folder = get_folder_from_request(request, folder_name, create=True)
    folder.item_set.create(content_object=obj)
