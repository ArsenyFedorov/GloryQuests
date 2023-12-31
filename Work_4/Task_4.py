# Николай – оригинальный человек.  Он решил создать класс Nikola, принимающий при инициализации 2 параметра:
# имя и возраст. Но на этом он не успокоился. Не важно, какое имя передаст пользователь при создании экземпляра,
# оно всегда будет содержать “Николая”. В частности - если пользователя на самом деле зовут Николаем,
# то с именем ничего не произойдет, а если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
# Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то и вздумает
# так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество» или метод «приветствие»,
# то ничего у такого хитреца не получится).Для ограничения количества наборов свойств
# и методов в экземпляре применяется специальный магический атрибут __slots__.

class Nikola:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        if name != "Николай":
            self.name = f"Я не {name}, а Николай"
        else:
            self.name = name
        self.age = age


maks = Nikola("Maksim", 33)
print(maks.name, maks.age)

nikola = Nikola("Николай", 35)
print(nikola.name, nikola.age)
