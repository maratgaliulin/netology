class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade +=1

    def publish_grade(self) -> object:
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)

    def check_if_it_is_time_to_upgrade(self):
        pass