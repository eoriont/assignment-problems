# include <iostream>

int main() {
  int array[4] = {11, 12, 13, 14};

  std::cout << "Array has address: " << &array << "\n";

  for (int i = 0; i < sizeof(array)/sizeof(array[0]); i++) {
    std::cout << "Index " << i << " has value " << array[i] << " and address " << &array[i] << "\n";
  }

  return 0;
}
