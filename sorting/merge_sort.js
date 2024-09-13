const merge = (arr1, arr2) => {
  const results = [];
  let index1 = 0;
  let index2 = 0;

  while(index1 < arr1.length && index2 < arr2.length) {
    if (arr1[index1] <= arr2[index2]) {
      results.push(arr1[index1])
      index1 ++
    }
    else {
      results.push(arr2[index2])
      index2 ++
    }
  }

/*   while(index1 < arr1.length) {
    results.push(arr1[index1])
    index1++
  }

  while(index2 < arr2.length) {
    results.push(arr2[index2])
    index2++
  } */

  results.push(...arr1.slice(index1), ...arr2.slice(index2));
  return results;
}


const mergeSort = (arr) => {
  if(arr.length <= 1) return arr;
  let midpoint = Math.floor(arr.length/2);
  const leftArr = mergeSort(arr.slice(0,mid));
  const rightArr = mergeSort(arr.slice(mid));
  return merge(leftArr, rightArr)
}