from abc import ABC, abstractmethod


class INotification(ABC):
    @abstractmethod
    def send(self, title: str, message: str):
        raise NotImplementedError()


class EmailNotification(INotification):
    def __init__(self, admin_email: str):
        self.__admin_email = admin_email

    def send(self, title: str, message: str) -> None:
        print('Sent email with title: %s, message: %s' % (title, message))


class SlackApi(object):
    def __init__(self, login: str, api_key: str):
        self.__login = login
        self.__api_key = api_key

    def login(self) -> None:
        print('Loggen in to slack {login}'.format(login=self.__login))

    def send_message(self, chat_id: str, message: str) -> None:
        print('Posted message into {}:{}'.format(chat_id, message))


class SlackNotification(INotification):
    def __init__(self, slack: SlackApi, chat_id: str):
        self.__slack = slack
        self.__chat_id = chat_id

    def send(self, title: str, message: str) -> None:
        slack_message = '#' + title + '#' + message
        self.__slack.login()
        self.__slack.send_message(self.__chat_id, slack_message)


def client_code(notification: INotification):
    title = 'Some title'
    message = 'Some message'

    notification.send(title, message)


if __name__ == '__main__':
    notification = EmailNotification('develper@example.com')
    client_code(notification)

    slack_api = SlackApi('example', '****')
    notification = SlackNotification(slack_api, 'Developers')
    client_code(notification)
