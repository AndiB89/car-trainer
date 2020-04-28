
ALTER SEQUENCE car_car_id_seq RESTART WITH 1

TRUNCATE TABLE "car_car" CASCADE;

INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('A Kompaktlimousine' , 'A' , 'W177' , 42983 , 2020 , true , 'img/1.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('B Klasse Sports Tourer' , 'B' , 'W247' , 0 , 2020 , true , 'img/2.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('C Klasse T-Modell' , 'C' , 'S205' , 0 , 2020 , true , 'img/3.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('E Klasse T-Modell' , 'E' , 'S213' , 0 , 2020 , true , 'img/4.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('CLA Shooting brake' , 'CLA' , 'X118' , 0 , 2020 , true , 'img/5.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('A Klasse Limousine' , 'A' , 'V177' , 0 , 2020 , true , 'img/6.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('C Klasse Limousine' , 'C' , 'W205' , 0 , 2020 , true , 'img/7.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('E Klasse Limousine' , 'E' , 'W213' , 0 , 2020 , true , 'img/8.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('S Klasse Limousine' , 'S' , 'W222' , 0 , 2020 , true , 'img/9.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('Maybach S Klasse Limousine' , 'S' , 'X222' , 0 , 2020 , true , 'img/10.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('C Klasse Coupé' , 'C' , 'C205' , 0 , 2020 , true , 'img/11.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('E Klasse Coupé' , 'E' , 'C238' , 0 , 2020 , true , 'img/12.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('S Klasse Coupé' , 'C' , 'C217' , 0 , 2020 , true , 'img/13.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('CLA Coupé' , 'CLA' , 'C118' , 0 , 2020 , true , 'img/14.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('CLS Coupé' , 'CLS' , 'C257' , 0 , 2020 , true , 'img/15.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('AMG GT Coupé' , 'GT' , 'C190' , 0 , 2020 , true , 'img/16.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('AMG GT 4-Türer Coupé' , 'GT' , 'X290' , 0 , 2020 , true , 'img/17.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('EQC' , 'EQC' , 'N293' , 0 , 2020 , true , 'img/18.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('G Klasse Geländewagen' , 'G' , 'W463' , 0 , 2020 , true , 'img/19.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('GLA SUV' , 'GLA' , 'H247' , 0 , 2020 , true , 'img/20.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('GLB SUV' , 'GLE' , 'X247' , 0 , 2020 , true , 'img/21.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('GLC SUV' , 'GLC' , 'X253' , 0 , 2020 , true , 'img/22.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('GLE SUV' , 'GLE' , 'V167' , 0 , 2020 , true , 'img/23.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('GLS SUV' , 'GLS' , 'X167' , 0 , 2020 , true , 'img/24.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('GLC Coupé' , 'GLC' , 'C253' , 0 , 2020 , true , 'img/25.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('GLE Coupé' , 'GLE' , 'C167' , 0 , 2020 , true , 'img/26.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('SLC Roadster' , 'SLC' , 'R172' , 0 , 2020 , true , 'img/27.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('SL Roadster' , 'SLC' , 'R231' , 0 , 2020 , true , 'img/28.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('C Klasse Cabriolet' , 'C' , 'A205' , 0 , 2020 , true , 'img/29.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('E Klasse Cabriolet' , 'E' , 'A238' , 0 , 2020 , true , 'img/30.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('S Klasse Carbiolet' , 'S' , 'A217' , 0 , 2020 , true , 'img/31.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('AMG GT Roadster' , 'GT' , 'R190' , 0 , 2020 , true , 'img/32.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('X Klasse Pickup' , 'X' , 'X250' , 0 , 2020 , true , 'img/33.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('EQV' , 'EQV' , '447' , 0 , 2020 , true , 'img/34.jpg');
INSERT INTO "car_car" ("name", "class_name", "series", "price", "releaseYear", "isStillProduced", "image") VALUES ('V Klasse Großraumlimousine' , 'V' , '447' , 0 , 2020 , true , 'img/35.jpg');

SELECT * FROM "car_car" LIMIT 1000;
