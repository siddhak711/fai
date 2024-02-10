let availableKeywords = [
    'Reedy High School',
    'Frisco High School',
    'Lebanon Trail High School',
    'Wakeland High Schoool',
    'Manchester Essex Regional High School',
    'Pine Crest High School',
    'North Broward Prep High School',
    'Dr. Michael Krop Senior High School',
    'Abraham Lincoln High School',
    'Saratoga High School',
    'Bellarmine College Prepatory',
    'New Tech High @ Coppell',
    'Hebron High School',
    'Prosper High School',
    'Lewisville High School - Harmon',
    'Flower Mound HS',
    'Francis Howell North',
    'The Adelson School',
    'Ed W. Clark High School',
    'The Meadows School',
    'Montclair High School',
    'Pioneer Heritage Middle School',
    'Griffin Middle School',
    'Green Level High School',
    'Heritage High School',
    'Ray Braswell High School',
    'Centennial High School',
    'Panther Creek High School',
    'Cypress Ranch High School',
    'Cypress Ranch High School',
    'North Allegheny Senior High School',
    'North Allegheny Intermediate High School',
    'Parsippany Hills High School',
    'Pine-Richland High School',
    'Roy C. Ketcham	High School',
    'Benjamin Franklin High School',
    'Gyanodaya International School',
    'Y. B. Patil Polytechnic',
    'BASIS International School Guangzhou',
    'Guangzhou Tianxin Experimental School',
    'Beijing Academy',
    'Shanghai Guanghua Cambridge International School',
    'Ulink College of Shanghai',
    'The Woodlands High School',
    'Lone Star High School',
    'Central High School',

];

const resultsBox = document.getElementById("result-box");
const inputBox = document.getElementById("input-box");

inputBox.onkeyup = function(){
    let result = [];
    let input = inputBox.value;
    if(input.length){
        result = availableKeywords.filter((keyword)=>{
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
    }
    display(result);

    if(!result.length){
        resultsBox.innerHTML = '';
        resultsBox.classList.add('hidden');
    }
}

function display(result){
    const content = result.map((list)=>{
        return `<li class='py-2 px-2 hover:text-white hover:bg-gray-800 hover:bg-opacity-60 rounded-md transition cursor-pointer list-none'>${list}</li>`;
    });

    resultsBox.innerHTML = content.join('');
    
    if (result.length > 0) {
        resultsBox.classList.remove('hidden');
        resultsBox.classList.add('mt-2'); // Add margin top when there are results
    } else {
        resultsBox.classList.add('hidden');
        resultsBox.classList.remove('mt-2'); // Remove margin top when there are no results
    }
}

function selectInput(list){
    inputBox.value = list.innerHTML;
    resultsBox.innerHTML = '';
    resultsBox.classList.add('hidden');
}
