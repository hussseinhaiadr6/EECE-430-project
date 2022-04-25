function $(id){
	return document.getElementById(id);
}
var checked =true 
window.onload = () => 

        {   
            psw1=document.getElementById("psw1");
            psw2=document.getElementById("psw2");
            psw2.onmouseout=()=>{
                if ( psw1.value!=psw2.value){
                    psw2.style.backgroundColor="red";
                  $("error").innerHTML=" password doesn't match";
                }

            }
        console.log("it worked man enjoy")
        form =$("submit")
        form.onclick=(event)=>{
            email=document.getElementById("email");
            psw1=document.getElementById("psw1");
            psw2=document.getElementById("psw2");
          
            console.log(pname.value);
            console.log(id.value);
            console.log(pdoc.value);
           
            
            if ( pname.value==""||id.value ==  "" ||page.value ==""||pdoc.value ==""){
                
                
                event.preventDefault();
                if( pname.value==""){
                alert(" name field is empty");}
                else {if( page.value==""){
                alert(" age  field is empty");}else{
                if( id.value==""){
                alert("  id field is empty");}else {
                if( pdoc.value==""){
                alert(" pdoc  field is empty");};}}}		
            }
        };
};
