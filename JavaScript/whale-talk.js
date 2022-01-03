const input = 'Its holiday time!';
const vowels = ['a', 'e', 'i', 'o', 'u'];
let resultArray = [];

for (let inputIndex = 0; inputIndex < input.length; inputIndex++) {
  // console.log('Input Index = ' + inputIndex);
  for (let vowelsIndex = 0; vowelsIndex < vowels.length; vowelsIndex++) {
   //  console.log(vowelsIndex);
   if (input[inputIndex] === vowels[vowelsIndex]){
     if(input[inputIndex] === 'e'){
       resultArray.push('ee')
     }
     else if(input[inputIndex] === 'u') {
       resultArray.push('uu');
     }
     else {
       resultArray.push(input[inputIndex])
     }
   }
  }
}

console.log(resultArray.join("").toUpperCase());