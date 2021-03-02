# include <iostream>
# include <cassert>

int calcIndex(int n) {
  // For first 2 indices
  if (n < 0) {
    return 0;
  } else if (n < 1) {
    return 1;
  }
  int a = 0;
  int b = 1;
  int index = 2;
  // Loop until we find a match
  while (true) {
    // Calc new value
    int newval = a + b;
    a = b;
    b = newval;
    // If new value is greater than n, return
    if (n < b) {
      return index;
    }
    index++;
  }
}

int main() {
    std::cout << "Testing...\n";

    assert(calcIndex(8)==7);
    assert(calcIndex(100000)==26);

    std::cout << "Success!";

    return 0;
}
