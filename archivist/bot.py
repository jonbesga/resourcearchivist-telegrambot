import logging
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from telegram.messageentity import MessageEntity

from archivist import handlers
from archivist.handlers import error_handler

logger = logging.getLogger(__name__)

updater = None


def __get_updater(token):
    global updater
    if not updater:
        updater = Updater(token=token)
        return updater
    return updater


def setup_and_configure_bot(token):
    dispatcher = __get_updater(token).dispatcher

    resources_handler = MessageHandler(
        Filters.entity(MessageEntity.URL),
        handlers.archive_resource
    )
    dispatcher.add_handler(resources_handler)
    dispatcher.add_error_handler(error_handler)

    return updater
