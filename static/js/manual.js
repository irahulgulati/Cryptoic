function msg(){
    if (document.getElementById("ptext").type == "hidden" && document.getElementById("ptext").value.length != 0) {
        document.getElementById("ptext").type = 'show';
        document.getElementById("decrypt").disabled = true;
        document.getElementById("decryptlabel").style.display = 'block';
      } 
    else{
            document.getElementById("ptext").type	 = 'hidden';
            alert("Please encrypt first");
        }

}