
package lab10;

/**
 *
 * @author morgan
 */
public class brittLab10 {
    public static void main(String[] args) {
int[] arr = new int[]{1, 2, 3, 4, 5, 6, 7, 8};
}
  
private static void displayArray(int[] arr, int index) {
if(index == arr.length){
System.out.println();
return;
}
System.out.print(arr[index] + " ");
displayArray(arr, index + 1);
}
  
public static void displayArray(int index, int[] arr) {
displayArray(arr,0);
}

//displayReverse method
private static void displayReverse(String s) {
if((s == null)||(s.length() <= 1))
System.out.println(s);
else{
System.out.print(s.charAt(s.length() - 1));
displayReverse(s.substring(0,s.length() - 1));
}
}
  
private static int factorial(int n) {
if (n == 0)
return 1;
return n*factorial(n - 1);
}

//dispalyArrayIndex method
private static void displayArrayIndex(int[] arr,int current,int first,int middle, int last) {
System.out.print("F" + " ");
for(int i=1 ; i<=middle - first - 1; i++){
System.out.print(" ");
}
System.out.print("M" + " ");
for(int i=1 ; i<last-middle; i++){
System.out.print(" ");
}
System.out.print("L");
System.out.println();
}

//binarySearch
private static int binarySearch(int [] arr,int low,int high,int value) {
if(high >= low){
int mid = low + (high-low)/2;
//Displays array in order
displayArray(0, arr);
displayArrayIndex(arr, mid, low, mid, high);
  
if(arr[mid] == value)
return mid;
if(arr[mid] > value)
return binarySearch(arr, low, mid-1, value);
return binarySearch(arr, mid+1, high, value);
}
return -1;
}

//binarySearch method
public static int binarySearch(int[] arr,int value) {
displayArray(0,arr);
displayArrayIndex(arr,0,0,arr.length/2,arr.length-1);
return binarySearch(arr,0,arr.length-1,value);
}

//Swap method
private static void swap(int[] arr,int i, int j) {
int temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
}

//Private partition method
private static int partition(int[] arr,int low,int high) {
int pivot = arr[high];
int i = (low-1);
for(int j = low; j <= high-1; j++){
if(arr[j] < pivot){
i++;
swap(arr, i, j);
}
}
swap(arr, i + 1, high);
return(i+1);
}

//Private quickSort method
private static void quickSort(int[] arr, int low, int high) {
if(low < high){
int pi = partition(arr, low, high);
quickSort(arr, low, pi - 1);
quickSort(arr, pi + 1, high);
}
displayArray(0, arr);
}
}