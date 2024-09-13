const getDigit = (number, place) => {
  return Math.floor(Math.abs(number)/Math.pow(10, place) % 10) 
}

const digitCount = (number) => {
  if (number === 0) return 1;
  return Math.floor(Math.log10(Math.abs(number))) + 1
}

const mostDigits = (arr) => {
  let maxDigits = 0;
  for (let number of arr) {
    maxDigits = Math.max(maxDigits, digitCount(number));
  }
  return maxDigits
}

const radixSort = (arr) => {
  let maxDigitCount = mostDigits(arr)
  for (let i = 0; i < maxDigitCount; i++) {
    let digitBuckets = Array.from({length: 10}, () => [])
    for (let number of arr) {
      finalDigit = getDigit(number, i);
      digitBuckets[finalDigit].push(number)
    }
    arr = [].concat(...digitBuckets)
    console.log(arr)
  }
}

radixSort([23,345,5467,12,2345,9852])

