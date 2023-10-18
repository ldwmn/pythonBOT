class Student:
    '''
ДК
    '''
    def __init__(self, name, age, fav_subj, grade):
        '''

        :param name:
        :param age:
        :param fav_subj:
        :param grade:
        '''

        self.name = name
        self.age = age
        self.fav_subj = fav_subj
        self.grade = grade

    def says_hello(self):
        '''

        :return:
        '''
        print(f'Hello {self.name}')


    def hit(self):
        '''

        :return:
        '''
        if self.fav_subj == 'Информатика':
            print(f'{self.name} в порядка')

        else:
            print(f'{self.name} не любил информатику, его жестоко избили')

student1 = Student('Иван', 16, 'Иванов', 'Информатика')
student2 = Student('Иван', 16, 'Иванов', 'c')