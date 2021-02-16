# include <iostream>
# include <cassert>
int main() {
  int array[5]{ 30, 50, 20, 10, 40 };

  for (int i = 0; i < 5; i++) {
    for (int j = i; j < 5; j++) {
      if (array[i] > array[j]) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }

  std::cout << "Testing...\n";

  assert(array[0]==10);
  assert(array[1]==20);
  assert(array[2]==30);
  assert(array[3]==40);
  assert(array[4]==50);

  std::cout << "Succeeded";

  return 0;
}
