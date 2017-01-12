#include <stdio.h>
int removeElement(int a[], int n, int elem)
{
    int i, num = n;
    for (i = 0; i < n; ++i)
        if (a[i] == elem)
            num--;
    return num;
}

int main(int argc, char const *argv[])
{
    int n, a[100], elem, i;
    scanf("%d", &n);
    for (i = 0; i < n; ++i)
        scanf("%d", &a[i]);
    scanf("%d", &elem);
    printf("%d\n", removeElement(a, n, elem));
    return 0;
}