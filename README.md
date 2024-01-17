# Алгоритмы для систем АВР (Автоматический Ввод Резерва)

### Требования к АВР

* Обеспечение подачи питания потребителю электроэнергии от резервного ввода, если произошло непредвиденное прекращение работы основной линии.
* Максимально быстрое восстановление электропитания.
* Обязательная однократность действия. То есть, недопустимо несколько включений-отключений нагрузки из-за КЗ или по иным причинам.
* Включение выключателя основного питания должно производиться автоматикой АВР до подачи резервного электропитания.
* Система АВР должна контролировать цепь управления резервным оборудованием на предмет исправности.

### Устройство АВР

* **Одностороннее**. В таких АВР один ввод играет роль рабочего, то есть используется, пока в линии не возникнут проблемы. Второй – является резервным, и подключается, когда в этом возникает необходимость.
* **Двухстороннее**. В этом случае нет разделения на рабочую и резервную секцию, поскольку оба ввода имеют одинаковый приоритет.

## Описание

Файлы конфигурации (как готовое решение) для систем АВР на ПЛК (программируемые логические контроллеры):
* Zelio
* Owen
* Logo8!
* Oni ...

### Типы АВР
2 ввода с секционированием <br>
2 ввода с секционированием + генератор<br>
2 ввода без секционирования<br>
2 ввода без секционирования + генератор<br>

### Передача данных по сети **Modbus** (RTU, TCP):
* Возможность дистанцинной блокировки АВР (активация дистанционного управления)
* Управление автоматическими выключателями в дистанционном режиме
* Система мониторинга в реальном времени за процесом работы

### Панели оператора:
* Ведение журнала событий
* Уровень доступа к данным
* Мнемосхема и состояние работы

[Запуск и настройка проекта](Settings.md)
