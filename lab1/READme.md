# Реализация небольшой сети офиса

Конфигурации можно посмотреть в папке [node-configs](node-configs). Также прикладываю лабораторную [hse-lab1.unl](hse-lab1.unl).

- Собрала сеть с такой топологией:
<!-- ![topology](images/topology.png) -->
<img src="images/topology.png" width="400">

- Настройки vlan можно посмотреть в конфигах.
- Здесь на левой картинке видно, что коммутатор уровня распределения (switch3) является корнем для обоих vlan, а на правой картинке - скрин с терминала switch2, на котором видно, что соединение между коммутаторами уровня доступа заблокировалось в результате работы протокола STP.

<img src="images/switch3-spanning-tree.png" height="400"> <img src="images/switch2-spanning-tree.png" height="400">

- Пинги от client1 к client2, и наоборот:

<img src="images/ping-1.png" height="200"> <img src="images/ping-2.png" height="200">
