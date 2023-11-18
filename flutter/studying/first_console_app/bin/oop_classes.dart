class User {
  late String name;
  late int age ;
  late bool isHappy ;
  late List<String> hobbies;
  void display() {
    print('Name: $name. Age: $age. isHappy: $isHappy. Hobbies: ${hobbies.join(', ')}');
  }

  User([name, age, isHappy, hobbies]) {
    this.name = name;
    this.age = age;
    this.isHappy = isHappy;
    this.hobbies = hobbies;
  }
}

void main() {
  var bob = User('Bob', 15, true, ['football', 'baseball']);
  bob.display();
}
 