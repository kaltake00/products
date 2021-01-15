# products
Zadatak za zadaću.

Zadatak glasi : 
Zamislite da je potrebno da modelujete informacioni sistem jedne trgovine.
Potrebno je da napravite klasu Product koja će predstavljati osnovu za dalje
nasleđivanje i neće se moći instancirati. Ovu klasu nasleđuju dve klase koje
predstavljaju konkretne grupe proizvoda: Chocolate i Wine. 
Svaki proizvod poseduje određene osobine:
naziv proizvoda,
bar-kod (obična numerička vrednost),
osnovnu cenu,
porez.
Takođe, svaki proizvod poseduje i metodu za računanje cene, koja se izračunava kada se osnovna cena i uveća
za iznos poreza. Porez (PDV) za svaki proizvod je 20% i ovo je podatak koji je konstantan i neće se menjati.
Ipak, proizvodi iz grupe vina, imaju i dodatni porez, pošto spadaju u grupu alkoholnih pića i on iznosi 10% od cene već
uvećane za iznos PDV-a. I ovo je podatak koji je konstantan i neće se menjati.
Zbog ovoga je potrebno redefinisati metodu za računanje cene u okviru klase Wine.
Pored ovoga, klasa Wine treba da poseduje atribut koji definiše zapreminu boce, a klasa Chocolate atribut koji definiše
težinu.
U klasama Chocolate i Wine, potrebno je napraviti parametrizovane konstruktore za kreiranje
objekata. Potrebno je, takođe, u klasama redefinisati metodu str za prikaz informacija o objektu.

![alt text](https://prnt.sc/wqdmxc)
