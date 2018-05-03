// What is working: 1. If you put in value for 1 to 4 search criteria, the result only matches with that search criteria.
//                  2. If you search with a criteria that has more than 50 results, like country of us. Page 1,2,3,4
//                     will show the results for those pages. 
//                  3. Each page only shows 50 results. When the page loads, it shows 10 results only.
// What is not working: The pagination previous and next button doen't work.

// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $stateInput = document.querySelector("#datetime");
var $cityInput = document.querySelector("#city");
var $state2Input = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");

renderPagination();
var $page1Btn = document.querySelector("#\\31");
var $page2Btn = document.querySelector("#\\32");
var $page3Btn = document.querySelector("#\\33");
var $page4Btn = document.querySelector("#\\34");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);
$page1Btn.addEventListener("click", handleSearchButtonClick);
$page1Btn.myParam = "button1"
$page2Btn.addEventListener("click", handleSearchButtonClick);
$page2Btn.myParam = "button2"
$page3Btn.addEventListener("click", handleSearchButtonClick);
$page3Btn.myParam = "button3"
$page4Btn.addEventListener("click", handleSearchButtonClick);
$page4Btn.myParam = "button4"
// Set filteredAddresses to addressData initially
var filteredAddresses = dataSet.splice(0, 10);
var len = filteredAddresses.length;

function renderPagination() {
  // numPages=Math.floor(len/50)+1
  var pageList = document.querySelector("ul");
  for (var i = 1; i < 5; i++) {

    // Empty String to hold HTML
    var pageItem = document.createElement("li")
    // Update todoListItem's innerHTML w/ the text of the todo object
    //<li><a href="www.google">Lena</a> </li>
    var aItem = document.createElement("a")
    // aItem.setAttribute("href", "www.google.com")
    aItem.setAttribute("id", i)
    aItem.innerHTML = i
    pageItem.append(aItem);
    // Add todo to the list
    pageList.appendChild(pageItem);


  }

}


// renderTable renders the filteredAddresses to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredAddresses.length; i++) {
    // Get get the current address object and its fields
    var address = filteredAddresses[i];
    var fields = Object.keys(address);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = address[field];
    }
  }
}

function handleSearchButtonClick(evt) {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCity = $cityInput.value.trim().toLowerCase();
  var filterState2 = $state2Input.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();

  var spliceIdx = 0;
  var spliceHowMany = 50;
  if (evt.target.myParam == 'button1') {
    spliceIdx = 0;
    spliceHowMany = 50;
  } else if (evt.target.myParam == 'button2') {
    spliceIdx = 50;
    spliceHowMany = 50;
  } else if (evt.target.myParam == 'button3') {
    spliceIdx = 100;
    spliceHowMany = 50;
  } else if (evt.target.myParam == 'button4') {
    spliceIdx = 150;
    spliceHowMany = 50;
  } 

  // else if (evt.target.myParam == 'button3') {
  //   spliceIdx = 100;
  //   spliceHowMany = 50;
  // }
// Set filteredAddresses to an array of all addresses whose "state" matches the filter
filteredAddresses = dataSet.filter(function (address) {
  // if (filterState!=""){var addressState = address.datetime.toLowerCase();}
  // if (filterCity!=""){var addressCity = address.city.toLowerCase();}
  // if (filterState2!=""){var addressState2 = address.state.toLowerCase();}
  // if (filterCountry!=""){var addressCountry = address.country.toLowerCase();}
  // if (filterShape!=""){var addressShape = address.shape.toLowerCase();}
  var addressState = address.datetime.toLowerCase();
  var addressCity = address.city.toLowerCase();
  var addressState2 = address.state.toLowerCase();
  var addressCountry = address.country.toLowerCase();
  var addressShape = address.shape.toLowerCase();

  // If true, add the address to the filteredAddresses, otherwise don't add it to filteredAddresses
  arr1 = [filterState, filterCity, filterState2, filterCountry, filterShape]
  arr2 = [addressState, addressCity, addressState2, addressCountry, addressShape]
  new_arr1 = []
  new_arr2 = []
  //check if non-null filter
  var nonNullArrayIdx = []
  for (var j = 0; j < 5; j++) {
    if (arr1[j] != "") {
      nonNullArrayIdx.push(j)
      new_arr1.push(arr1[j])
      new_arr2.push(arr2[j])
    }
  }

  for (var j = 0; j < nonNullArrayIdx.length; j++) {
    if (j == 0) { result = (new_arr1[0] === new_arr2[0]) }
    else { result = result && (new_arr1[j] === new_arr2[j]) }
  }
  return result;
}).splice(spliceIdx, spliceHowMany);
// filteredAddresses=filteredAddresses.splice(0,50)
renderTable();
}

// Render the table for the first time on page load

renderTable();