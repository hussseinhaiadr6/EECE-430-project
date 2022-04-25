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
        
      }
    

}
        
        
