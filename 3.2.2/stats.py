@@ -77,7 +77,7 @@ class Salary:
 salary_to (float): Верхняя граница вилки оклада
        salary_currency (str): Валюта оклада
    """
    def __init__(self, salary_from, salary_to, salary_gross, salary_currency):
    def __init__(self, salary_from, salary_to, salary_currency):
        """Инициализирует объект Salary
        Args:
@@ -87,7 +87,6 @@ def __init__(self, salary_from, salary_to, salary_gross, salary_currency):
        """
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_gross = salary_gross
        self.salary_currency = salary_currency


@@ -472,14 +471,12 @@ def generate_pdf(self, filename='report.pdf'):
        pdfkit.from_string(html, filename, options={"enable-local-file-access": None})


def main():
def main(file, name):
    """
    Входная точка программы.
    Получает на вход путь к файлу и название профессии, генерирует по ним статистику и сохраняет отчет во всех
    возможных форматах.
    """
    file = input('Введите название файла: ')
    name = input('Введите название профессии: ')
    dataset = DataSetReader(file).read()

    stats = Statistics(dataset, name)
@@ -491,4 +488,6 @@ def main():


if __name__ == '__main__':
    main()
    file = input('Введите название файла: ')
    name = input('Введите название профессии: ')
    main(file, name)