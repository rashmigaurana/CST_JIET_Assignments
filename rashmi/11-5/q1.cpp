
#include <iostream> 
using namespace std; 
int findSingle(int arr[], int arr_size) 
    { 
        int result= arr[0]; 
        for (int i = 1; i < arr_size; i++) 
            result = result ^ arr[i]; 
        return result; 
    } 
int main() 
    {
    	int arr[ ]={2,2,3,4,5,4,5};
        int n = sizeof(arr) / sizeof(arr[0]); 
        cout << "Element occurring once is " 
             << findSingle(arr, n); 
        return 0;
    }
