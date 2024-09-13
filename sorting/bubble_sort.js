//bubble sorting bubbles the max value all the way to the end of the array
const swap =require( "./swap")

const bubbleSort = (arr) => {
  let noSwaps;
  for (let i = arr.length - 1; i >= 0; i--) {
    noSwaps = true
    for (let j = 0; j < i; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1)
        noSwaps = false
      }
    }

    if (noSwaps) break;
  }
  return arr
}

const list = [23, 4, 56, 7, 89, 10, 3, 67]
const list2 = [8, 1, 2, 3, 4, 5, 6, 7]

console.log(bubbleSort(list))
console.log(bubbleSort(list2))


