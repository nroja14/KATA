function switchList(numbers, s){
    let reversedList = []
    for(let i = numbers.length -1; i >= 0; i--){
        currentNumber = numbers[i];
        numberDigits = currentNumber.toString().split('')
        let newDigits = []
        
        for(digit of numberDigits){
            if(digit < s.toString()){
                newDigits.push(digit)
            }
        }

        newNumberString = newDigits.join('')

        if(newNumberString){
            newNumber = parseInt(newNumberString)
            reversedList.push(newNumber)
            }
        }
    return reversedList;
}

const numbers =  [60, 6, 5, 4, 3, 2, 7, 7, 29, 1] 
result = switchList(numbers, 5)
console.log(result)