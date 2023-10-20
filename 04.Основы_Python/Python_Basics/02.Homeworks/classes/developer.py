from .employee import Employee

class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)

    def check_if_it_is_time_to_upgrade(self):
        # Для каждой аккредитации увеличиваем счетчик на 1
        # Пока считаем что все разработчики проходят аккредитацию
        self.seniority += 1

        # Условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()

        # Публикация результатов
        return self.publish_grade()