from abc import ABC, abstractmethod


class ISocialNetworkConnector(ABC):
    @abstractmethod
    def login(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def logout(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def create_post(self, content: str) -> None:
        raise NotImplementedError()


class FacebookConnector(ISocialNetworkConnector):
    def __init__(self, login: str, password: str):
        self.__login = login
        self.__password = password

    def login(self) -> None:
        print(f"Logging in with {self.__login} and {self.__password}")

    def logout(self) -> None:
        print(f"Logging out from Facebook")

    def create_post(self, content: str) -> None:
        print('Creating post in Facebook')


class LinkedInConnector(ISocialNetworkConnector):
    def __init__(self, email: str, password: str):
        self.__email = email
        self.__password = password

    def login(self) -> None:
        print(f'Logging in with {self.__email} and {self.__password}')

    def logout(self) -> None:
        print('Logging out from LinkedIn')

    def create_post(self, content: str) -> None:
        print('Creating post in LinkedIn')


class SocialNetworkPoster(ABC):
    @abstractmethod
    def get_social_network(self) -> ISocialNetworkConnector:
        raise NotImplementedError()

    def post(self, content: str) -> None:
        network = self.get_social_network()

        network.login()
        network.create_post(content)
        network.logout()


class FacebookParser(SocialNetworkPoster):
    def __init__(self, login: str, password: str):
        self.__login = login
        self.__password = password

    def get_social_network(self) -> ISocialNetworkConnector:
        return FacebookConnector(self.__login, self.__password)


class LinkedInParser(SocialNetworkPoster):
    def __init__(self, email: str, password: str):
        self.__email = email
        self.__password = password

    def get_social_network(self) -> ISocialNetworkConnector:
        return LinkedInConnector(self.__email, self.__password)


def create_post_in_social_network(social_network: SocialNetworkPoster, content: str) -> None:
    social_network.post(content)


if __name__ == '__main__':
    create_post_in_social_network(FacebookParser('login', '****'), 'content in facebook')
    print('-' * 20)
    create_post_in_social_network(LinkedInParser('email', '****'), 'content in linkedin')
