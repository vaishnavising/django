console.log("title is working");

// var = x;
// for(x =0; x<=5; x++){
// console.log          
// 

// }
function validateform(){
  x= document.forms["myform"]['email'].value;
  if(x==""){
            document.getElementById('email1').placeholder= "enter your email";
            document.getElementById('email1').style.border ="2px solid red";
            var x = document.getElementById('valid');
            x.innerHTML ="enter your email";
            x.style.color = "red";
            return false;

 }

  }
  function crElement(){
            x = document.getElementByIdClassName("myname");
            console.log(x);

      x[0].innerHTML = "heyyyy";   
      x= document.createElement("input"); 
      z = document.createElement("label");
      x.setAttribute("class","myname");
      y =document.getElementById("mydiv");
      y.appendChild(x);
      y.appendChild(z);
  }
