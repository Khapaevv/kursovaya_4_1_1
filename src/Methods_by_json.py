from abc import ABC, abstractmethod
from src.Vacancy_class import Vacancy
import json

class AbstractClass(ABC):
    pass


    @abstractmethod
    def add_vacancy_like_atr(cls, vac_name):
        cls.vac_name = vac_name



    @abstractmethod
    def get_data_from_name(cls, key_word, list):
        pass


    @abstractmethod
    def get_data_from_requirement(cls, key_word, list):
        pass


    @abstractmethod
    def delete_vacancy_if_not_key_word(cls, key_word):
        pass


class ClassForChange(AbstractClass):
    """класс для добавления объектов класса Vacancy в файл и других методов"""


    def __init__(cls, vac_name = ''):
        cls.__vac_name = vac_name


    @classmethod
    def add_vacancy_like_atr(cls, vac_name):
        """Метод добавляет объекты класса Vacancy в файл {vac_name}_vacancies.json из файла
         (в котором находятся вся информация по ключевому слову ваканcии)"""
        cls.__vac_name = vac_name
        list_vacancies = []
        with open("./data/vacancies.json", "r", encoding='utf-8') as file:
            items = json.load(file)['items']
            for item in items:
                if item.get("salary") is not None:
                    vacancy = Vacancy(item.get("name"), item.get("alternate_url"), item.get("salary"),
                                      item["snippet"].get("requirement"))
                else:
                    vacancy = Vacancy(item.get("name"), item.get("alternate_url"), None,
                                      item["snippet"].get("requirement"))
                list_vacancies.append(vacancy.__dict__)
            with open(f'./data/{vac_name}_vacancies.json', 'w+', encoding='utf-8') as file:
                json.dump(list_vacancies, file, sort_keys=True, indent=4, ensure_ascii=False)


    @classmethod
    def sort_objects_by_salary(cls, vac_name):
        """Метод сортировки вакансий по зарплате в порядке возрастания"""
        sorted_salary = []
        with open(f'./data/{vac_name}_vacancies.json', 'r', encoding='utf-8') as file:
            file = json.load(file)
            sorted_salary = sorted(file, key=lambda object: object['salary'], reverse=True)
        return sorted_salary


    @classmethod
    def top_by_salary(cls, vac_name, len_top):
        top = []
        top = cls.sort_objects_by_salary(vac_name)[:len_top]
        return top


    @classmethod
    def get_data_from_name(cls, key_word, list):
        """Метод для фильтрации вакансий по ключевому слову в названии, выводит список"""
        filtered_from_name = []
        for object in list:
            if key_word in object['name']:
                filtered_from_name.append(object)
        return filtered_from_name


    @classmethod
    def get_data_from_requirement(cls, key_word, list):
        filtered_from_requirement = []
        """Метод для фильтрации вакансий по ключевому слову в описании,
         из списка, полученного после get_data_from_name выводит новыый список"""
        for object in list:
            if object['requirement'] is not None:
                if key_word in object['requirement']:
                    filtered_from_requirement.append(object)
        return filtered_from_requirement


    @classmethod
    def delete_vacancy_if_not_key_word(cls, key_word):
        cls.add_vacancy_like_atr()
        updated_vacancies = []
        """Метод удаления объектов класса Vacancy, если в них нет ключевого слова"""
        with open('./data/{cls.vac_name}_vacancies.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        updated_vacancies = [vacancy for vacancy in data if vacancy.get('name') != key_word]
        with open('./data/del_vacancies_like_atr.json', "w", encoding="utf-8") as f:
            json.dump(updated_vacancies, f, indent=4, ensure_ascii=False)