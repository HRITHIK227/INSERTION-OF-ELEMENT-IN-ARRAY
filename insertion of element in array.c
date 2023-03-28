#include <stdio.h>

int main() {
    int arr[100];  // Declare an array of size 100
    int n, pos, val;

    // Read the number of elements in the array
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    // Read the elements of the array
    printf("Enter the elements of the array:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Read the position and value of the element to be inserted
    printf("Enter the position where you want to insert the element: ");
    scanf("%d", &pos);
    printf("Enter the value of the element: ");
    scanf("%d", &val);

    // Shift the elements of the array to the right from the specified position
    for (int i = n - 1; i >= pos; i--) {
        arr[i+1] = arr[i];
    }

    // Insert the element at the specified position
    arr[pos] = val;

    // Increment the size of the array
    n++;

    // Print the updated array
    printf("The updated array is:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
