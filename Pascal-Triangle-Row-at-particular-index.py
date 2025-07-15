#include <iostream>
using namespace std;

void pascalRow(int Index) {
    const int MAX = 100;
    int row[MAX] = {0};
    row[0] = 1;

    for (int i = 1; i <= Index; ++i) {
        for (int j = i; j > 0; --j) {
            row[j] = row[j] + row[j - 1];
        }
    }

    cout << "Pascal Row " << Index << ": ";
    for (int i = 0; i <= Index; ++i) {
        cout << row[i] << " ";
    }
    cout << endl;
}

int main() {
    int Index;
    cout << "Enter row index: ";
    cin >> Index;

    if (Index >= 0 && Index < 100)
        pascalRow(rowIndex);
    else
        cout << "Row index too large!" << endl;

    return 0;
}
