
import 'dart:io';
import 'dart:math';
void main(List<String> arguments) {
  stdout.write("Певое число");
  int num1 = int.parse(stdin.readLineSync()!);
  stdout.write("Второе число");
  int num2 = int.parse(stdin.readLineSync()!);
  stdout.write("Введите знак: +, -, *, /, ~/, %, pow, ==, !=, >, <, >=, <=, &&, ||, !");
  String opp = stdin.readLineSync() !;

  if (opp == "+"){
    print ("$num1 + $num2 = ${num1+ num2}");
  } else if (opp == "-") {
    print("$num1 - $num2 = ${num1 - num2}");
    
  } else if (opp == "*") {
    print("$num1 * $num2 = ${num1 * num2}");
    
  } else if (opp == "/") {
    if (num2 != 0) {
      double result = num1 / num2;
      print("$num1 / $num2 = $result");
    } else {
      print("Ошибка: деление на ноль");
    }
    
  } else if (opp == "~/") {
    if (num2 != 0) {
      print("$num1 ~/ $num2 = ${num1 ~/ num2}");
    } else {
      print("Ошибка: деление на ноль");
    }
    
  } else if (opp == "%") {
    if (num2 != 0) {
      print("$num1 % $num2 = ${num1 % num2}");
    } else {
      print("Ошибка: деление на ноль");
    }
    
  } else if (opp.toLowerCase() == "pow") {
    num result = pow(num1, num2);
    print("$num1 в степени $num2 = $result");
    
  } else if (opp == "==") {
    print("$num1 == $num2: ${num1 == num2}");
    
  } else if (opp == "!=") {
    print("$num1 != $num2: ${num1 != num2}");
    
  } else if (opp == ">") {
    print("$num1 > $num2: ${num1 > num2}");
    
  } else if (opp == "<") {
    print("$num1 < $num2: ${num1 < num2}");
    
  } else if (opp == ">=") {
    print("$num1 >= $num2: ${num1 >= num2}");
    
  } else if (opp == "<=") {
    print("$num1 <= $num2: ${num1 <= num2}");
    
  } else if (opp == "&&") {
    bool bool1 = num1 != 0;
    bool bool2 = num2 != 0;
    print("$num1 && $num2 = ${bool1 && bool2}");
    
  } else if (opp == "||") {
    bool bool1 = num1 != 0;
    bool bool2 = num2 != 0;
    print("$num1 || $num2 = ${bool1 || bool2}");
    
  } else if (opp == "!") {
    bool value = num1 != 0;
    print("!$value = ${!value}");
    
  } else {
    print("Неизвестная операция: $opp");
  }
}


