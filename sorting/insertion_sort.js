const insertionSort = (arr) => {
  for (let i = 1; i <arr.length; i++) {
    let currentVal = arr[i]
    for(var j = i - 1; j >= 0 && arr[j] > currentVal; j--) {
      arr[j+1] = arr[j]
    }
    arr[j+1] = currentVal;
  }
  return arr;
}

const list = [23, 4, 56, 7, 89, 10, 3, 67]
const list2 = [8, 1, 2, 3, 4, 5, 6, 7]

console.log(insertionSort(list))
console.log(insertionSort(list2))
