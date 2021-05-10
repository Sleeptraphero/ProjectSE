function toggleMenu(){
    const menuToggle = document.querySelector('.toggle');
    const sidebar = document.querySelector('.sidebar');
    menuToggle.classList.toggle('active');
    sidebar.classList.toggle('active');
}

function darkMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
  }

function smoothScroll(target){
    var element = document.getElementById(target)
    if(typeof(element) != 'undefined' && element != null){
        element.scrollIntoView();
    } else{ 
        window.location.replace("/")
    }
}
function validateForm(){
	var fname = document.forms["newsltForm"]["fname"].value;
    var lname = document.forms["newsltForm"]["lname"].value;
	var email = document.forms["newsltForm"]["email"].value;

	if (fname.length<1) {
        document.getElementById('error-fname').innerHTML = " Please enter your first name *"
    }
    if (email.length<1) {
        document.getElementById('error-lname').innerHTML = " Please enter your last name *";
    }
    if (email.length<1) {
        document.getElementById('error-email').innerHTML = " Please enter your email adress *";      
    }
    if(fname.length<1 || lname.length<1 || email.length<1){
       	return false;
    }            
}