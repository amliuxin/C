#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char const *argv[])
{
    long long n, m, a;
    long long i, j;
    cin >> n >> m >> a;
    i = ceil((double)n / (double)a);
    j = ceil((double)m / (double)a);
    cout << i * j << endl;
    return 0;
}