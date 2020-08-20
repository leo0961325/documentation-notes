from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """
    觀察者/訂閱者
    """
    @abstractmethod
    def update(self, water_degree: float) -> None:
        raise NotImplementedError


class Observable(metaclass=ABCMeta):
    """
    發佈者
    """
    @abstractmethod
    def add_observer(self, ob: Observer):
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, ob: Observer):
        raise NotImplementedError

    @abstractmethod
    def notify_observers(self):
        raise NotImplementedError


class WaterHeater(Observable):
    """
    熱水器
    """
    __observers = []
    __degree: float = 20.0

    def add_observer(self, ob: Observer) -> None:
        self.__observers.append(ob)

    def remove_observer(self, ob: Observer) -> None:
        self.__observers.remove(ob)

    def notify_observers(self) -> None:
        for ob in self.__observers:
            ob.update(water_degree=self.__degree)

    def set_degree(self, degree: float = 0.0) -> None:
        if degree > 70:
            self.__degree = 70
        elif degree < 0:
            self.__degree = 0
        else:
            self.__degree = degree
        
        self.notify_observers()

    def get_degree(self) -> float:
        return self.__degree


class Father(Observer):
    is_taking_shower: bool = False

    def update(self, water_degree: float) -> None:
        if water_degree <= 20:
            self.__take_shower()

    def __take_shower(self) -> None:
        self.is_taking_shower = True


class GrandPa(Observer):
    is_taking_shower: bool = False

    def update(self, water_degree: float) -> None:
        if water_degree >= 50:
            self.__take_shower()

    def __take_shower(self) -> None:
        self.is_taking_shower = True
