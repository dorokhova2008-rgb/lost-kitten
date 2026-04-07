import 'dart:convert';
import 'dart:io';
import 'dart:math';
import 'package:characters/characters.dart';
import 'package:dart_application_3/dart_application_3.dart' as dart_application_3;

enum Mood{
  happy,
  sad,
  cool
}

void main(List<String> arguments) {
  stdout.write("Введите ваше имя: ");
  String name = stdin.readLineSync(encoding: utf8)!;
  print("Генерируем случайное настроение");
  Random rand = Random();
  Mood mood = Mood.values[rand.nextInt(Mood.values.length)];

  String emoji = "";
  String text = "";
  int energy = 0;

  if (mood == Mood.happy) {
    emoji = "😊";
    // print(emoji.runes);
    // print(emoji.runes.first.toRadixString(16));
    // String sm="1f60a";
    print(String.fromCharCode(128522));
    text = "радостный";
    energy = 8;
  }
  

  if (mood == Mood.sad) {
    emoji = "😢";
    // print(emoji.runes);
    // print(emoji.runes.first.toRadixString(16));
    // // String sm="1f60e";
    print(String.fromCharCode(128526));
    text = "грустный";
    energy = 3;
  }

  if (mood == Mood.cool) {
    emoji = "😎";
    // print(emoji.runes);
    // print(emoji.runes.first.toRadixString(16));
    // String sm="1f60e";
    print(String.fromCharCode(128526));
    text = "взволнованный";
    energy = 9;
  }

  print("Привет, $name! Твое настроение: $emoji $text (энергия: $energy/10)");
  print("Юникод вашего эмодзи: U+${emoji.runes.first.toRadixString(16)}");
  stdout.write("Хотите просмотреть сложные эмодзи? (да/нет): ");
  String answer = stdin.readLineSync(encoding: utf8)!;

  if (answer == "да") {
    stdout.write("Введите комбинацию эмодзи: ");
    String smiles = stdin.readLineSync(encoding: utf8)!;
  
  print('Анализ строки "$smiles":');
  print("- 16-битных единиц: ${smiles.length}");
  print("- Кодовых точек: ${smiles.runes.length}");
  print("- Реальных символов: ${smiles.characters.length}");
  print("Подробный вывод юникода:");
  int i = 1;
  for (var rune in smiles.runes) {
    print("Символ $i: ${String.fromCharCode(rune)} -- U+${rune.toRadixString(16)}");
    i++;
  }
}
}
  // String smile="😛";
  // print(smile.runes);
  // print(smile.runes.first.toRadixString(16));

  // String sm="1f61b";
  // print(sm);

  // print(String.fromCharCode(128539));
  // // print(smile.runes.length);
  // // print(sm.length);


