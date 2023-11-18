// void main() {
//   var a = 15, b = 15;
//   if (a > b || a == b) {
//     print('a > b');
//   } else if (a == b) {
//     print('a = b');
//   } else if (a < b) {
//     print('a < b');
//   } else {
//     print(false);
//   }
// }
// == != > < >= <=
// && это соединение для двух условий т.е and
// || или or
void main() {
  var a = 20;
  var res = 0;
  if (a == 5) {
    res = 10;
  } else {
    res = 20;
  }
  print(res);
  var b = a == 5 ? 10 : 20;
  // если а = 5 то б присвоить 10 иначе 20
  print(b);
  var digit = 5;
  switch (digit) {
    case 4:
      print('equal 4');
      break;
    case 5:
      print('equal 5');
      break;
    case 6:
      print('equal 6');
      break;
    default:
      print('>5');
  }
}
