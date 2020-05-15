$(document).ready(function(){
  $('.tabs').tabs({
   swipeable:true,
   responsiveThreshold: 700
  });
  
});

var proxyUrl ='https://cors-anywhere.herokuapp.com/',
    url="http://www.recipepuppy.com/api/"


async function getData(proxyUrl, url){
  try{
    let response = await fetch(proxyUrl + url);
    let result= await response.json();
    drawtable(result.results)
    console.log(result.results)
  }
catch(e){
  console.log(e);

}
}

function Add(){
 
  while(list[i] != null){
  ingredients.innerHTML +=`<tr>
  <div class="items">
   
    <label>
    <input id="indeterminate-checkbox" type="checkbox" />
    <span>${list[i]} </span>
  </label> 
  </div>
    `;
    i=i+1;
  }
  // console.log(list);
}
var list=[];
var i=0;
getData(proxyUrl, url)

function drawtable(recipes){
  let result = document.querySelector('#result');
  for(let recipe of recipes){
    list=recipe.ingredients; 
    list= list.split(',')
    // console.log(list);
    result.innerHTML +=`<tr>
    <div class="items">
     
      <h4>${recipe.title}</h4> 
      <img src=${recipe.thumbnail} width:100px height:100px </img>
      <br>
      <a>${recipe.href}</a>
      <li>${recipe.ingredients}</li>
      <button type ='button'  onclick ='Add(list)' >ADD</button>
      
      </tr>
      </div>
      <br>`;
  }
}

