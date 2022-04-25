function $(id){
	return document.getElementById(id);
}
var checked =true 
window.onload = () =>  {
    DelayNode
    var Tds= document.getElementsByTagName("td")
    var pattern=/^no/
    console.log(Tds[17].innerHTML)
    for (let i = 0; i < Tds.length; i++) {
        console.log(Tds[i].value)
        if (pattern.test(Tds[i].innerHTML)){
            Tds[i].style.backgroundColor="black"}
        else{
            if(Tds[i].id){
            var br=document.createElement("br")
            var a = document.createElement('a');
            a.style.color='black';
            a.style.backgroundColor="#e11";
            a.style.borderRadius="1em";
            a.style.padding="5px";
            a.style.marginTop="20px";
            a.class="reserve";
            var linkText = document.createTextNode("reserve");
            a.appendChild(linkText);
            a.title = "my title text";
            var st="http://localhost:8000/reserveclass/id=";
            var st1 =st+Tds[i].id;
            a.href = st1;
            Tds[i].appendChild(br);
            Tds[i].appendChild(br);
            Tds[i].appendChild(a);
            }


        }

      }
    

}
        
        
