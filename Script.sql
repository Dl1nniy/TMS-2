1.Создать бд sheltor
CREATE DATABASE sheltor


2.Создать таблицу animal со следующими полями:
id, имя животного, тип животного, возраст, пол, вес

USE sheltor;
CREATE TABLE animal(
    id_animal int NOT NULL AUTO_INCREMENT,
    name_animal varchar(255),
    pyte_animal varchar(255),
    age_animal int,
    sex_animal varchar(255),
    weight_animal int,
    PRIMARY KEY (id_animal)
);

3.Добавить в эту таблицу несколько животных
INSERT INTO animal (name_animal,pyte_animal,age_animal,sex_animal,weight_animal) VALUES ('барбос','собака','7','мужской','8');
INSERT INTO animal (name_animal,pyte_animal,age_animal,sex_animal,weight_animal) VALUES ('барсик','кот','3','мужской','4');
INSERT INTO animal (name_animal,pyte_animal,age_animal,sex_animal,weight_animal) VALUES ('кеша','попугай','2','женский','1');
INSERT INTO animal (name_animal,pyte_animal,age_animal,sex_animal,weight_animal) VALUES ('кролик','бони','1','женский','2');
INSERT INTO animal (name_animal,pyte_animal,age_animal,sex_animal,weight_animal) VALUES ('мурзик','кот','2','мужской','3');


4.Выполнить следующие запросы:
4.1.Узнать количество животных в приюте
SELECT COUNT(*) FROM animal;


4.3 Узнать количество собак в приюте
SELECT COUNT(*) FROM animal WHERE pyte_animal LIKE 'собака';

4.4 Узнать средний вес собак в приюте
SELECT avg(weight_animal) FROM animal where pyte_animal='собака';

4.5 Узнать какие типы животных есть (например, собаки и коты)
SELECT DISTINCT pyte_animal FROM animal;

4.6 Узнать сколько в приюте животных с именем Вилли
SELECT COUNT(*) FROM animal WHERE name_animal LIKE 'Вилли'

4.7 Узнать количество собак - особей женского и мужского пола
SELECT COUNT(*) FROM animal WHERE pyte_animal LIKE 'собака' and sex_animal LIKE 'мужской';
SELECT COUNT(*) FROM animal WHERE pyte_animal LIKE 'собака' and sex_animal LIKE 'женский';

4.8 Вывести список уникальных имен котов и вывести его в алфавитном порядке
SELECT  DISTINCT name_animal FROM animal WHERE pyte_animal = 'кот';

4.9 Вывести всех животных, у которых имя заканчивается на “ик”
SELECT *
FROM animal
WHERE name_animal LIKE '%ик'

4.10 Заменить имя Барсик у всех записей на Монти
USE sheltor;
UPDATE animal
SET name_animal='Монти' WHERE name_animal='барсик';

