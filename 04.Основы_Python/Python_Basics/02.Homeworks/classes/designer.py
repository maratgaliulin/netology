from .employee import Employee

class Designer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)



    def check_if_it_is_time_to_upgrade(self, award = False):
        # Для каждой аккредитации увеличиваем счетчик на 1
        # Пока считаем что все разработчики проходят аккредитацию
        if not award:
            self.seniority += 1
        elif award:
            self.seniority += 2

        # Условие повышения сотрудника из презентации
        self.grade = int(self.seniority / 7 + 1)

        # Публикация результатов
        return self.publish_grade()

