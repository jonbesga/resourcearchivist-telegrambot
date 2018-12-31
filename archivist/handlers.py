import logging
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)

from archivist import resources

logger = logging.getLogger(__name__)


def error_handler(bot, update, error):
    try:
        raise error
    except Unauthorized:
        logger.error(error, update)
    except BadRequest:
        pass
    except TimedOut:
        pass
    except NetworkError:
        pass
    except ChatMigrated:
        pass
    except TelegramError:
        pass


def archive_resource(bot, update):
    message = update.message
    resource = resources.get_resource(message)
    bot.sendMessage(chat_id=resource.channel, text=message.text)
