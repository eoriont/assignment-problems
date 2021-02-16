# include <iostream>
# include <cassert>
# include <vector>

int listSum(int len, int* list) {
  int res = 0;
  for (int i = 0; i <= len; i++) {
    res += list[i];
  }
  return res;
}

int* seqList(int n) {
  int* arr = new int[n];
  for (int i = 0; i <= n; i++) {
    if (i < 2) {
      arr[i] = i;
    } else {
      arr[i] = arr[i-1] + 2*arr[i-2];
    }
  }
  return arr;
}

int* extendSeqList(int newLength, int initialLength, int* seqlist) {
  int* newarr = new int[newLength];
  for (int i = 0; i <= newLength; i++) {
    if (i < initialLength) {
      newarr[i] = seqlist[i];
    } else {
      newarr[i] = newarr[i-1] + 2*newarr[i-2];
    }
  }
  return newarr;
}

int seqSum(int n) {
    int* seqlist = seqList(n);
    int sum = listSum(n, seqlist);
    delete [] seqlist;
    return sum;
}

int extendedSeqSum(int n) {
    int* seqlist = seqList(n);
    int* extendedseqlist = extendSeqList(seqlist[n], n, seqlist);
    int sum = listSum(seqlist[n], extendedseqlist);
    delete [] seqlist;
    delete [] extendedseqlist;
    return sum;
}


int main() {
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!";

    return 0;
}
