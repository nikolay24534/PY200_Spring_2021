from typing import Any, Sequence, Optional


class LinkedList:
    """
    Класс, определяющий связный список
    """

    class Node:
        """
        Внутренний класс, класса LinkedList.

        Пользователь напрямую не работает с узлами списка, узлами оперирует список.
        """

        def __init__(self, value: Any, next_: Optional['LinkedList.Node'] = None):
            """
            Создаем новый узел для односвязного списка

            :param value: Любое значение, которое помещено в узел
            :param next_: следующий узел, если он есть
            """
            self.value = value
            self.next = next_  # Вызывается сеттер

        @property
        def next(self):
            """Getter возвращает следующий узел связного списка"""
            return self.__next

        @next.setter
        def next(self, next_: Optional['LinkedList.Node']):
            """Setter проверяет и устанавливает следующий узел связного списка"""
            if not isinstance(next_, self.__class__) and next_ is not None:
                msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                      f"или None, не {next_.__class__.__name__}"
                raise TypeError(msg)
            self.__next = next_

        def __repr__(self):
            """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
            return f"Node({self.value}, {self.next})"

        def __str__(self):
            """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
            return f"{self.value}"

    def __init__(self, data: Sequence = None):
        """
        Конструктор связного списка

        :param data: Sequence
            последовательность
        """
        self.__len = 0
        self.head = None  # Node

        if data:
            for value in data:
                self.append(value)

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        result = [value for value in self]
        return f"{result}"

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        result = [value for value in self]
        return f"LinkedList({result})"
        # return f"{type(self).__name__}({result})"

    def __len__(self):
        """
        Метод, возвращающий длину списка

        :return:
            длина связного списка
        """
        return self.__len

    def __getitem__(self, item: int) -> Any:
        """
        Метод, возвращающий элемент связного списка по индексу

        :param item: int
            индекс элемента, который мы хотим вернуть
        :return:

        """
        if not isinstance(item, int):
            raise TypeError('Я умею принимать только целые числа')

        if not 0 <= item < self.__len:
            raise IndexError()

        current_node = self.head
        for _ in range(item):
            current_node = current_node.next

        return current_node.value

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Метод, изменяющий элемент в связном списке по индексу

        :param key: int
            индекс элемента
        :param value: Any
            значение элемента
        :return:
            None
        """
        if not isinstance(key, int):
            raise TypeError('Я умею принимать только целые числа')

        if not 0 <= key < self.__len:
            raise IndexError()

        current_node = self.head
        for _ in range(key):
            current_node = current_node.next

        current_node.value = value

    def append(self, value: Any) -> None:
        """
        Добавление элемента в конец связного списка

        :param value: Any
            добавляемый в конец элемент
        :return:
            None
        """
        append_node = self.Node(value)
        if self.head is None:
            self.head = append_node
        else:
            tail = self.head  # ToDo Завести атрибут self.tail, который будет хранить последний узел
            for _ in range(self.__len - 1):
                tail = tail.next
            self.__linked_nodes(tail, append_node)

        self.__len += 1

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def to_list(self) -> list:
        """
        Метод, преобразующий свзяный списко в объект типа list

        :return: list
            Преобразрванный к типу list связный список
        """
        return [value for value in self]

    def insert(self, index: int, value: Any) -> None:
        """
        Метод, добавляющий элемент в связный список по заданному индексу

        :param index: int
            индекс элемента вставки
        :param value: Any
            значение элемента вставки
        :return:
            None
        """
        if index == 0:
            insert_node = self.Node(value)
            ex_head = self.head
            self.__linked_nodes(insert_node, ex_head)
            self.head = insert_node
            self.__len += 1

        elif 1 <= index <= self.__len - 1:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next

            up_insert_node = current_node.next
            insert_node = self.Node(value)
            self.__linked_nodes(current_node, insert_node)
            self.__linked_nodes(insert_node, up_insert_node)
            self.__len += 1

        elif index >= self.__len:
            self.append(value)

    def clear(self) -> None:
        """
        Метод, удаляющий все эелемнты связного списка

        :return:
            None
        """
        self.head = None
        self.__len = 0

    def index(self, value: Any) -> int:
        """
        Возвращает индекс переданного значения

        :param value:
            значение индекс которого нужно получить
        :return: int
            индекс заданного значения
        """
        current_node = self.head
        if current_node.value == value:
            return 0

        for i in range(1, self.__len):
            current_node = current_node.next
            if current_node.value == value:
                return i
        else:
            raise ValueError(f'{value} is not in list')

    def remove(self, value: Any) -> None:
        """
        Метод, который удлает значение из связного списка

        :param value: Any
            Знчение, которое нужно удалить из связного списка
        :return:
            None
        """
        current_node = self.head
        if current_node.value == value:
            new_head = current_node.next
            del current_node
            self.head = new_head
            self.__len -= 1
            return None

        for _ in range(self.__len - 1):
            next_node = current_node.next
            if next_node.value == value:
                self.__linked_nodes(current_node, next_node.next)
                del next_node
                self.__len -= 1
                break
            current_node = current_node.next

        else:
            raise ValueError(f'list.remove({value}): {value} not in list')

    def sort(self) -> None:
        """
        Сортирует связный список сортировкой пузырьком

        :return:
            None
        """
        flag = True
        current_node = self.head

        while flag:
            flag = False
            for _ in range(1, self.__len - 1):
                next_node = current_node.next
                if next_node is None:
                    current_node = self.head
                    flag = True
                    break
                if current_node.value > next_node.value:
                    flag = True
                    current_node.value, next_node.value = next_node.value, current_node.value
                current_node = current_node.next

    def is_iterable(self, data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        return hasattr(self, '__iter__')


if __name__ == '__main__':
    ll = LinkedList([3, 1, 9, 2])
    print(ll)
    ll.insert(2, 99)
    print(ll)
    ll.sort()
    print(ll)
    ll.clear()
    print(ll)
