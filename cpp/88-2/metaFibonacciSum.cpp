# include <iostream>
# include <cassert>
# include <vector>

int fib(int n) {
    if (n < 2) {
        return n;
    }
    return fib(n-1) + fib(n-2);
}

int fibSum(int n) {
    int result = 0;
    for (int i = 0; i <= n; i++) {
        result += fib(i);
    }
    return result;
}

int metaFibonacciSum(int n) {
    int result = 0;
    for (int i = 0; i <= n; i++) {
        result += fibSum(fib(i));
    }
    return result;
}

int main() {
    std::cout << "Testing...\n";
    assert(metaFibonacciSum(6)==74);

    std::cout << "Success!";

    return 0;
}
