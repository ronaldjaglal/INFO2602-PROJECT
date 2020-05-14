$(document).ready(function(){
  $('.tabs').tabs({
   swipeable:true,
   responsiveThreshold: 700
  });
  
});




// let pokemon =[ {name:"", website:"",}];

//  let Recipedata = {
//      title:"",
//      href:"",
//      ingredients:"",
//      thumbnail:"",
     
// } ;



// async function getData(url){
//   try{
//     let response = await fetch(url);
//     console.log(url)
    
//      let result = await response.json();
//      for (i = 0; i <10; i++){
//      recipes[i]= result.results[i];
   
//      }
//   }catch(e){
//     console.log(e);

//   }
// }




//  const detail = document.querySelector('.detail');

//  const masterItems = document.querySelectorAll('.collection-item');

// masterItems.forEach((item) => {
//   item.addEventListener('click', function(){
//     console.log("clicked");
//     for(let item of masterItems){
//       //console.log(item.id);
//       item.classList.remove('active-item');
    
    
//     }

//     this.classList.add('active-item');
    
  


//     for(i=0; i<50;i++){ ;
//  if(item.id == recipes[i].name){
//    //console.log(pokemon[i].name);
// recipes[i].website = "http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3"+recipes[i].name;
//       let url1 = recipes[i].website;
// console.log(url1);

// async function getDetails(url1){
//         try{
//         let responses= await fetch(url1);
//         let details = await responses.json();
//           Recipedata.title= details.title;
//           Recipedata.href=details.href;
//           Recipedata.ingredients=details.ingredients;
//           Recipedata.thumbnail=details.thumbnail;
//         //   Recipedata.type=details.types[0].type.name;
//         //   pokemonData.sprite=details.sprites.front_default;
          
//               detail.innerHTML= `   <img src=${Recipedata.thumbnail} widhth= 400px height= 400px></img>
//                                           <li>${Recipedata.title}</li>
//                                           <li>Ingredients: ${Recipedata.ingredients}</li>
//                                           <li>Href: ${Recipedata.href}</li>
                                         
                         
//                                        `;

//          console.log(details.id);
//   }catch(e){
//     console.log(e);

//   }
//       };
//       getDetails(url1);
  
     
//  }};
   
 
  
//   });
// });


// let url="http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3";
//    getData(url);
