#include <iostream>
#include <cassert>

int calcSum(int m, int n) {
  int res = 0;
  for (int x = 0; x < m; x++) {
    for (int y = 0; y < m; y++) {
      for(int i = 0; i < n; i++) {
        res += (x*n+i+1) * (m*(n-i)-y);
      }
    }
  }
  return res;
}

int main() {
  std::cout << (calcSum(2, 3));
  assert(calcSum(2, 3)==131);
}
