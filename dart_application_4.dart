class Mug {
  int water;
  Mug(this.water);
}
class Human {
  String name;
  Human(this.name);

  void drink(Mug mug) {
    if (mug.water > 0) {
      print("$name выпил воду из кружки");
      mug.water = 0;
    } else {
      print("Кружка пустая");
    }
  }
}

class Wardrobe {
  List<String> things = [];
  void put(String thing) {
    things.add(thing);
    print("Положили в шкаф: $thing");
  }

  void take(String thing) {
    things.remove(thing);
    print("Забрали из шкафа: $thing");
  }
}

class Plate {
  int weight;
  Plate(this.weight);
}

class Bar {
  int maxWeight;
  List<Plate> plates = [];
  Bar(this.maxWeight);

  int currentWeight() {
    int sum = 0;
    for(var plate in plates){
      sum += plate.weight;
    }
    return sum;
  }

  void addPlate(Plate plate) {
    if (currentWeight() + plate.weight <= maxWeight) {
      plates.add(plate);
      print("Блин добавлен: ${plate.weight} кг");
    } else {
      print("Нельзя добавить блин");
    }
  }
}

class MoneyConverter {
  double dollarToRuble(double dollars) {
    return dollars * 90;
  }
  double rubleToDollar(double rubles) {
    return rubles / 90;
  }
}

class Garage<T> {
  List<T> items = [];

  void add(T item) {
    items.add(item);
    print("Добавлено в гараж: $item");
  }

  void remove(T item) {
    items.remove(item);
    print("Удалено из гаража: $item");
  }
}

class MyNumber {
  int value;
  MyNumber(this.value);
  MyNumber operator +(MyNumber other) {
    return MyNumber(value + other.value);
  }
  MyNumber operator -(MyNumber other) {
    return MyNumber(value - other.value);
  }
  MyNumber operator *(MyNumber other) {
    return MyNumber(value * other.value);
  }
  MyNumber operator /(MyNumber other) {
    return MyNumber(value ~/ other.value);
  }

  @override
  String toString() {
    return "$value";
  }
}

enum CarState {
  stop,
  drive,
  turn,
}

class Car {
  CarState state = CarState.stop;
  void drive() {
    state = CarState.drive;
    print("Машина едет");
  }

  void stop() {
    state = CarState.stop;
    print("Машина остановилась");
  }

  void turn() {
    state = CarState.turn;
    print("Машина повернула");
  }
}

abstract class Figure {
  double area();
}

class RectangleFigure extends Figure {
  double a;
  double b;
  RectangleFigure(this.a, this.b);

  @override
  double area() {
    return a * b;
  }
}

class TriangleFigure extends Figure {
  double a;
  double h;
  TriangleFigure(this.a, this.h);

  @override
  double area() {
    return a * h / 2;
  }
}

class CircleFigure extends Figure {
  double r;
  CircleFigure(this.r);

  @override
  double area() {
    return 3.14 * r * r;
  }
}

class NumberConverter {
  String convert(String number, int from, int to) {
    int decimal = int.parse(number, radix: from);
    return decimal.toRadixString(to);
  }
}

class FigureList {
  List<Figure> figures = [];

  void add(Figure figure) {
    figures.add(figure);
  }

  Figure maxAreaFigure() {
    Figure max = figures[0];
    for (var figure in figures) {
      if (figure.area() > max.area()) {
        max = figure;
      }
    }
    return max;
  }
}

class Cutlery {
  String name;
  Cutlery(this.name);

  @override
  String toString() {
    return name;
  }
}

class Spoon extends Cutlery {
  Spoon() : super("Ложка");
}

class Fork extends Cutlery {
  Fork() : super("Вилка");
}

class Knife extends Cutlery {
  Knife() : super("Нож");
}

class Table {
  List<Cutlery> items = [];

  void put(Cutlery item) {
    items.add(item);
    print("Положили на стол: $item");
  }

  void take(Cutlery item) {
    items.remove(item);
    print("Убрали со стола: $item");
  }
}
void main() {
  Mug mug = Mug(200);
  Human human = Human("Артём");
  human.drink(mug);

  Wardrobe wardrobe = Wardrobe();
  wardrobe.put("Футболка");
  wardrobe.put("Куртка");
  wardrobe.take("Футболка");

  Bar bar = Bar(50);
  bar.addPlate(Plate(10));
  bar.addPlate(Plate(20));
  print("Вес на грифе: ${bar.currentWeight()} кг");

  MoneyConverter converter = MoneyConverter();
  print("10 долларов = ${converter.dollarToRuble(10)} рублей");

  Garage<String> garage = Garage<String>();
  garage.add("Машина");
  garage.add("Мотоцикл");
  garage.remove("Мотоцикл");

  MyNumber a = MyNumber(10);
  MyNumber b = MyNumber(5);

  print(a + b);
  print(a - b);
  print(a * b);
  print(a / b);

  Car car = Car();
  car.drive();
  car.turn();
  car.stop();

  RectangleFigure rectangle = RectangleFigure(5, 4);
  TriangleFigure triangle = TriangleFigure(6, 3);
  CircleFigure circle = CircleFigure(3);

  print("Площадь прямоугольника: ${rectangle.area()}");
  print("Площадь треугольника: ${triangle.area()}");
  print("Площадь круга: ${circle.area()}");

  NumberConverter numberConverter = NumberConverter();
  print(numberConverter.convert("10", 10, 16));
  print(numberConverter.convert("A", 16, 10));

  FigureList list = FigureList();
  list.add(rectangle);
  list.add(triangle);
  list.add(circle);

  Figure maxFigure = list.maxAreaFigure();
  print("Максимальная площадь: ${maxFigure.area()}");

  Table table = Table();
  Spoon spoon = Spoon();
  Fork fork = Fork();
  Knife knife = Knife();

  table.put(spoon);
  table.put(fork);
  table.put(knife);
  table.take(fork);
}