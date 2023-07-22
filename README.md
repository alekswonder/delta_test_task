# Тестовое задание для DELTA:
### Ситуация:
Сделать небольшую социальную сеть для фотографов.

Есть страны, города, вещи, пользователи. Каждый тип имеет разный набор полей. <br>
Каждая сущность типа может иметь несколько фотографий. <br>
Фотография может быть как одобренная администратором, так и нет.
### Уточнение:
У каждой сущности может быть много фотографий. <br>
Сущности должны быть представлены в моделях. <br>
Сущности не должны дублироваться (город должен быть всегда один). <br>
Менеджер модели должен включать в себя метод получения фото _подчинённых_ моделей (страна включает в себя города, город - вещи, вещи - пользователей)

###### С помощью менеджеров нужно:
1) работать со всеми одобренными фото каждой сущности (получить все фото столов);
2) работать со всеми одобренными фото отдельного типа (получить все фото из Албании - и самой Албании, и столов, и стульев из неё);
3) работать со всеми неодобренными фото (чтобы вывести список для модераторов).

###### Что должно получиться:
Оптимальный набросок models.py django, с моделями и менеджерами, на основе которого будет ПРОЩЕ ВСЕГО развернуть rest api (DRF), которое бы позволило:
1) работать со всеми одобренными фото каждой сущности
2) работать со всеми одобренные фото отдельного типа
3) работать со всеми неодобренными фото