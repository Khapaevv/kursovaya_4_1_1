from abc import ABC, abstractmethod
import requests
import json


class Parser(ABC):
    """Класс Parser является абсрактным классом
    для всех поисковых платформ"""

    def __init__(self, vac_name):
        self.vac_name = vac_name

    @abstractmethod
    def load_vacancies(self, url):
        pass

class HHRussia(Parser):
    """Класс для работы с API HeadHunter России"""

    def __init__(self, vac_name):
        super().__init__(vac_name)


    def load_vacancies(self, url=None):
        """Метод вытаскивает вакансии по ключевому
        слову вакансии (только по России) и складывает в json"""
        url = 'https://api.hh.ru/vacancies?area=113'
        params = {
            'page': 0,
            'per_page': 100
        }
        response = requests.get(f'{url}&text={self.vac_name}', params)
        data = response.json()
        with open("./data/vacancies.json", "w", encoding='utf-8') as file:
            json.dump(data, file, sort_keys=True, indent=4, ensure_ascii=False)
        return data





