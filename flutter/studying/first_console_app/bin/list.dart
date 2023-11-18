// void main() {
//   var nums = [5, 7, 8, 3, 2];
//   nums.add(0); //добавить один элемент
//   nums.addAll([10, 11, 12]); //длбавить множество элементов
//   nums.remove(8); //удаление по значению
//   nums.removeAt(0); //удаление по индексу
//   nums.removeWhere((element) => element >= 5);//удалени е по условию
//   print(nums);
// }
void main() {
  var nums = [5, 7, 8, 3, 2, 20, 18, 4];
  print('First: ${nums[0]}, Last: ${nums.last}. Length: ${nums.length}');
  List nums2 = [1, 2, 3, 4, 5, 6];
  print(nums2);
  var digits = {1, 1, 1, 2, 3, 4, 5, 6};
  print(digits);
}
