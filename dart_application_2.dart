import 'package:dart_application_2/dart_application_2.dart' as dart_application_2;

void main(List<String> arguments) {

  List<String> students = ["Иван","Мария","Алексей","Ольга","Дмитрий","Анна" ];

  print("Список студентов:");
  for (int i = 0; i < students.length; i++) {
    print("${i + 1}. ${students[i]}");
  }
  List<String> subjects = ["Математика","Физика","Информатика","История"];

  print("Список предметов:");
  for (int i = 0; i < subjects.length; i++) {
    print("${i + 1} ${subjects[i]}");
  }
  List<List<int>> grades = [[5, 4, 5, 3], [4, 4, 5, 5], [3, 4, 4, 3], [5, 5, 5, 4], [2, 3, 4, 3], [4, 5, 4, 5]];
  
  print("Оценки студентов:");
  for (int i = 0; i < students.length; i++) {
    for (int j = 0; j < subjects.length; j++) {
      print("${students[i]} - ${subjects[j]}: ${grades[i][j]}");
    }
  }

  double sum;
  double avg;
  print("Средний балл по предметам:");
  for (int j = 0; j < subjects.length; j++) {
    double sum = 0;
    for (int i = 0; i < students.length; i++) {
      sum += grades[i][j];
    }
    double avg = sum / students.length;
    print("${subjects[j]}: $avg");
  }

  int summ;
  double avg_st;
  print("Средний балл студентов:");
  List<double> studentAverages = [];
  for (int i = 0; i < students.length; i++) {
    summ = grades[i].reduce((a, b) => a + b);
    avg = summ / subjects.length;
    studentAverages.add(avg);
    print("${students[i]}: $avg");
  }

  double maxAvg = studentAverages[0];
  int bestIndex = 0;
  for (int i = 1; i < studentAverages.length; i++) {
    if (studentAverages[i] > maxAvg) {
      maxAvg = studentAverages[i];
      bestIndex = i;
    }
  }
  print("Лучший студент: ${students[bestIndex]} $maxAvg");

double minAvg = 5;
int index = 0;
double sumi;
double avgGr;
for (int j = 0; j < subjects.length; j++) {
  sumi = 0;
  for (int i = 0; i < students.length; i++) {
    sumi += grades[i][j];
  }
   avgGr = sumi / students.length;
  if (avgGr < minAvg) {
    minAvg = avgGr;
    index = j;
  }
}
print("Предмет с наименьшим средним баллом: ${subjects[index]} $minAvg");

int summm = 0;
int count = 0;
for (int i = 0; i < students.length; i++) {
  for (int j = 0; j < subjects.length; j++) {
    summm += grades[i][j];
    count++;
  }
}
double avgRr = summm / count;
print("Общий средний балл группы: $avgRr");

Set unique = subjects.toSet();
print("Список предметов:");
for (var s in unique) {
  print(s);
}
print("Количество предметов: ${unique.length}");

print("Студенты без оценки 2:");
for (int i = 0; i < students.length; i++) {
  bool hasBad = false;
  for (int j = 0; j < subjects.length; j++) {
    if (grades[i][j] == 2) {
      hasBad = true;
    }
  }
  if (!hasBad) {
    print(students[i]);
  }
}

print("Студенты с оценками не ниже 4:");
for (int i = 0; i < students.length; i++) {
  bool good = true;
  for (int j = 0; j < subjects.length; j++) {
    if (grades[i][j] < 4) {
      good = false;
    }
  }
  if (good) {
    print(students[i]);
  }
}
}
