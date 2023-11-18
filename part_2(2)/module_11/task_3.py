class Parent:
    def __init__(self, name, age, childs=None):
        self.name = name
        self.age = age
        self.childs = childs
        self.check_childs()

    def info_parent(self):
        print(self.name, self.age, self.childs)

    def check_childs(self):
        for child in self.childs:
            if self.age - child.age < 16:
                print(f'{child.name} не может быть вашим ребенком.'
                      f' Программа удаляет его из вашего списка детей')
                self.childs.remove(child)

    def calm_child(self, child):
        if child.stat_calm:
            print(f'{self.name} успокаивает {child.name}')
            child.stat_calm = False

    def feed_child(self, child):
        if child.stat_hunger:
            print(f'{self.name} кормит {child.name}')
            child.stat_hunger = False


class Child:
    def __init__(self, name, age, calm, hunger):
        self.name = name
        self.age = age
        self.stat_calm = calm
        self.stat_hunger = hunger


def parent_babysit(parent):
    if len(parent.childs) == 0:
        print(f'У {parent.name} нет детей, ему не с кем водиться.')
        return
    for child in parent.childs:
        parent.calm_child(child)
        parent.feed_child(child)
