const swap =require( "./swap")

const pivot = (arr, start=0, end=arr.length+1) => {
  let pivot = arr[start];
  let sawpIndex = start;
  for (let i = start + 1; i < arr.length; i++) {
    if (pivot > arr[i]) {
      sawpIndex ++;
      swap(arr, sawpIndex, i)
    }
  }
  swap(arr,start,sawpIndex)
  return sawpIndex
}

const quickSort = (arr, left = 0, right = arr.lenght - 1) => {
  if (left < right) {
    let pivotIndex = pivot(arr, left, right)
    //left
    quickSort(arr, left, pivotIndex -1)
    //right
    quickSort(arr, pivotIndex + 1, right)
  }
  return arr;
}

console.log(pivot([4,8,2,1,5,7,6,3]))