#include <stdio.h>
#include <stdlib.h>

// Function to compare integers for qsort
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int arr[100];  // Assuming a max of 100 numbers
    int n = 0;

    // Read input numbers from stdin until newline (EOF)
    while (scanf("%d", &arr[n]) == 1) {
        n++;
    }

    // Sort the array
    qsort(arr, n, sizeof(int), compare);

    // Print sorted array
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
