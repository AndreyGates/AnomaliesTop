# AnomaliesTop
## Нахождение выбросов данных с наибольшим показателем аномальности

Модель, находящая топ-5 аномальных записей по набору параметров.<br>
Основана на алгоритме Isolation Forest, который эффективен для задач обучении без учителя.

## Установка репозитория
```
$ git clone https://github.com/AndreyGates/AnomaliesTop
```

## Установка необходимых библиотек
```
pip install -r requirements.txt
```

## Использование
Запустите файл anomaly_output.py для вывода номеров наиболее аномальных записей и их показателей аномальности, а также графика сжатых данных (с помощью PCA) для отображения выбросов.

## Автор
Andrey Pisarevsky\
E-mail: pisarevskiy1977@gmail.com

## Источники
* https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf
