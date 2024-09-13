//Selection sorting finds the min value and takes it to the begining of the array. 

const swap =require( "./swap")

const selectionSort = (arr) => {
  for(let i = 0; i < arr.length; i++) {
    let minIndex = i
    for(let j = i+1; j < arr.length; j++) {
      if(arr[minIndex] > arr[j]) {
        minIndex = j
      }
    }
    if (i !== minIndex) {
      swap(arr, i, minIndex)
    }
    
  }
  return arr
}

const list = [23, 4, 56, 7, 89, 10, 3, 67]
const list2 = [8, 1, 2, 3, 4, 5, 6, 7]

console.log(selectionSort(list))
console.log(selectionSort(list2))
